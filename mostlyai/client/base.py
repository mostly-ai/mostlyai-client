import os
import sys
import warnings
import webbrowser
from typing import (
    Annotated,
    Any,
    ClassVar,
    Generic,
    List,
    Literal,
    Optional,
    TypeVar,
    Union,
)

import httpx
import rich
from pydantic import BaseModel, ConfigDict, Field
from rich.console import Console

from mostlyai.client.exceptions import APIError, APIStatusError
from mostlyai.client.naming_conventions import (
    snake_to_camel,
    map_snake_to_camel_case,
    map_camel_to_snake_case,
)

GET = "GET"
POST = "POST"
PATCH = "PATCH"
DELETE = "DELETE"
HttpVerb = Literal[GET, POST, PATCH, DELETE]

DEFAULT_BASE_URL = "https://app.mostly.ai"
MAX_REQUEST_SIZE = 250_000_000

T = TypeVar("T")


class _MostlyBaseClient:
    """
    Base client class, which contains all the essentials to be used by subclasses.
    """

    API_SECTION = ["api", "v2"]
    SECTION = []

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: float = 60.0,
        ssl_verify: bool = True,
    ):
        self.base_url = (
            base_url or os.getenv("MOSTLY_BASE_URL") or DEFAULT_BASE_URL
        ).rstrip("/")
        self.api_key = api_key or os.getenv("MOSTLY_API_KEY")
        self.timeout = timeout
        self.ssl_verify = ssl_verify
        if not self.api_key:
            raise APIError(
                "The API key must be either set by passing api_key to the client or by specifying a "
                "MOSTLY_API_KEY environment variable"
            )

    def headers(self):
        return {
            "Accept": "application/json",
            "X-MOSTLY-API-KEY": self.api_key,
        }

    def request(
        self,
        path: Union[str, List[Any]],
        verb: HttpVerb,
        response_type: type = dict,
        raw_response: bool = False,
        is_api_call: bool = True,
        do_json_camel_case: bool = True,
        do_response_dict_snake_case: bool = True,
        do_include_client: bool = True,
        extra_key_values: Optional[dict] = None,
        **kwargs,
    ) -> Any:
        """
        Extended request helper method to send HTTP requests and process the response.

        Args:
            path (Union[str, List[Any]]): A single string or a list of parts of the path to concatenate.
            verb (HttpVerb): HTTP method (GET, POST, PATCH, DELETE).
            response_type (type): Type to cast the response into. Defaults to `dict`.
            raw_response (bool): Whether to return the raw response object. Defaults to `False`.
            is_api_call (bool): If `False`, skips prefixing API_SECTION and SECTION. Defaults to `True`.
            do_json_camel_case (bool): Convert the provided JSON to camelCase. Defaults to `True`.
            do_response_dict_snake_case (bool): Convert the response dictionary to snake_case. Defaults to `True`.
            do_include_client (bool): Include the client property in the returned object. Defaults to `True`.
            extra_key_values (dict, optional): Additional key-value pairs to include in the response object.
            **kwargs: Additional arguments passed to the HTTP request.

        Returns:
            Any: Processed response based on the `response_type`.

        Raises:
            APIStatusError: For HTTP errors (non-2XX responses).
            APIError: For network issues or request errors.
        """
        path_list = [path] if isinstance(path, str) else [str(p) for p in path]
        prefix = self.API_SECTION + self.SECTION if is_api_call else []
        full_path = [self.base_url] + prefix + path_list
        full_url = "/".join(full_path)

        kwargs["headers"] = self.headers() | kwargs.get("headers", {})

        if (request_size := _get_total_size(kwargs)) > MAX_REQUEST_SIZE:
            warnings.warn(
                f"The overall {request_size=} exceeds {MAX_REQUEST_SIZE}.", UserWarning
            )

        if "json" in kwargs and do_json_camel_case:
            if isinstance(kwargs["json"], BaseModel):
                kwargs["json"] = kwargs["json"].model_dump()
            kwargs["json"] = map_snake_to_camel_case(kwargs["json"])

        try:
            with httpx.Client(timeout=self.timeout, verify=self.ssl_verify) as client:
                response = client.request(method=verb, url=full_url, **kwargs)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            try:
                error_msg = exc.response.json()["message"]
            except Exception:
                error_msg = exc.response.content
            # Handle HTTP errors (not in 2XX range)
            raise APIStatusError(
                f"HTTP {exc.response.status_code}: {error_msg}",
            ) from exc
        except httpx.RequestError as exc:
            # Handle request errors (e.g., network issues)
            raise APIError(
                f"An error occurred while requesting {exc.request.url!r}."
            ) from exc

        if raw_response:
            return response

        if response.content:
            # this section could be split into a separate method
            response_json = response.json()
            if isinstance(response_json, dict) and not response_type == dict:
                if do_include_client:
                    response_json["client"] = self
                if isinstance(extra_key_values, dict):
                    response_json["extra_key_values"] = extra_key_values
            elif response_type == dict and do_response_dict_snake_case:
                response_json = map_camel_to_snake_case(response_json)
            return (
                response_type(**response_json)
                if isinstance(response_json, dict)
                else response_json
            )
        else:
            return None


class Paginator(Generic[T]):
    def __init__(self, request_context, object_class: T, **kwargs):
        """
        Generic paginator for listing objects with pagination.

        Args:
            request_context: The context in which the request function is called.
            object_class (T): Class of the objects to be listed.
            **kwargs: Additional filter parameters including 'offset' and 'limit'.
        """
        self.request_context = request_context
        self.object_class = object_class
        self.offset = kwargs.pop("offset", 0)
        self.limit = kwargs.pop("limit", 50)
        self.params = {snake_to_camel(k): v for k, v in kwargs.items()}
        self.current_items = []
        self.current_index = 0
        self.is_last_page = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Any cleanup if necessary
        pass

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if self.current_index >= len(self.current_items):
            self._fetch_data()
            self.current_index = 0
            if not self.current_items:
                raise StopIteration

        item = self.current_items[self.current_index]
        self.current_index += 1
        return self.object_class(**item, client=self.request_context, by_alias=True)

    def _fetch_data(self):
        if self.is_last_page:
            self.current_items = []

        params = {"offset": self.offset, "limit": self.limit}
        params.update(self.params)

        response = self.request_context.request(verb=GET, path=[], params=params)

        self.current_items = response.get("results", [])
        total_count = response.get("totalCount", 0)
        self.offset += self.limit

        if self.offset >= total_count:
            self.is_last_page = True


class CustomBaseModel(BaseModel):
    OPEN_URL_PARTS: ClassVar[list] = None  # ["d", "object-name"]
    client: Annotated[Optional[Any], Field(exclude=True, repr=False)] = None
    extra_key_values: Annotated[Optional[dict], Field(exclude=True, repr=False)] = None
    model_config = ConfigDict(protected_namespaces=(), populate_by_name=True)

    def _repr_html_(self):
        # Use rich.print to create a rich representation of the model
        console = Console()
        with console.capture() as capture:
            rich.print(self.model_dump())
        return capture.get()

    def open(self) -> str:
        """
        Opens the instance in a web browser.
        """
        if self.client is None or not self.OPEN_URL_PARTS or not hasattr(self, "id"):
            raise APIError("Cannot open the instance")
        url = "/".join([self.client.base_url, *self.OPEN_URL_PARTS, str(self.id)])
        webbrowser.open_new(url)
        return url


def _get_total_size(obj, seen=None):
    """Recursively finds size of objects in bytes."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Mark as seen *before* entering recursion to gracefully handle self-referential objects
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum(
            [
                _get_total_size(v, seen) + _get_total_size(k, seen)
                for k, v in obj.items()
            ]
        )

    elif hasattr(obj, "__dict__"):
        size += _get_total_size(obj.__dict__, seen)

    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([_get_total_size(i, seen) for i in obj])

    return size
