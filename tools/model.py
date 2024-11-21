from pathlib import Path
from typing import Annotated, Any, ClassVar, Literal, Optional, Union

import pandas as pd
from pydantic import Field

from mostlyai.model import JobProgress, SyntheticDatasetFormat, PermissionLevel


class Connector:
    OPEN_URL_PARTS: ClassVar[list] = ["d", "connectors"]

    def update(self, config) -> "Connector":
        """
        Update a connector, and optionally validate the connection before saving.

        If validation fails, a 400 status with an error message will be returned.

        For the structure of the config, secrets and ssl parameters, see the CREATE method.

        :return: The updated connector
        """
        return self.client._update(connector_id=self.id, config=config)

    def delete(self):
        """
        Delete connector
        """
        return self.client._delete(connector_id=self.id)

    def locations(self, prefix: str = "") -> list:
        """
        List connector locations

        List the available databases, schemas, tables or folders for a connector.
        For storage connectors, this returns list of folders and files at root, respectively at `prefix` level.
        For DB connectors, this returns list of schemas (or databases for DBs without schema), respectively list of tables if `prefix` is provided.

        The formats of the locations are:

        - Cloud storage:
            - `AZURE_STORAGE`: `container/path`
            - `GOOGLE_CLOUD_STORAGE`: `bucket/path`
            - `S3_STORAGE`: `bucket/path`
        - Database:
            - `BIGQUERY`: `dataset.table`
            - `DATABRICKS`: `schema.table`
            - `HIVE`: `database.table`
            - `MARIADB`: `database.table`
            - `MSSQL`: `schema.table`
            - `MYSQL`: `database.table`
            - `ORACLE`: `schema.table`
            - `POSTGRES`: `schema.table`
            - `SNOWFLAKE`: `schema.table`
        :param prefix: The prefix to filter the results by.
        :return: A list of locations (schemas, databases, directories, etc.) on the given level.
        """
        return self.client._locations(connector_id=self.id, prefix=prefix)

    def schema(self, location: str) -> list[dict[str, Any]]:
        """
        Retrieve the schema (column names, original data types and default model encoding types) of the table at a connector location.

        Please refer to `locations()` for the format of the location.

        :param location: The location of the table
        :return: The retrieved schema
        """
        return self.client._schema(connector_id=self.id, location=location)

    def config(self) -> dict[str, Any]:
        """
        Retrieve writeable generator properties

        :return: The generator properties as dictionary
        """
        return self.client._config(connector_id=self.id)

    def shares(self):
        """
        Retrieve list of shares

        :return: list of ResourceShares
        """
        return self.client._list_shares(resource_id=self.id)

    def share(
        self, user_email: str, permission_level: PermissionLevel = PermissionLevel.view
    ):
        """
        Share the connector with specified user and access rights (default PermissionLevel.view)
        """
        self.client._share(
            resource_id=self.id,
            user_email=user_email,
            permission_level=permission_level,
        )

    def unshare(self, user_email: str):
        """
        Stop sharing the connector with the specified user
        """
        self.client._unshare(resource_id=self.id, user_email=user_email)

    def share_public(self):
        """
        Share the connector with everyone
        """
        self.client._share_public(resource_id=self.id)

    def unshare_public(self):
        """
        Stop sharing the connector with everyone
        """
        self.client._unshare_public(resource_id=self.id)

    def like(self):
        """
        Like the connector
        """
        self.client._like(resource_id=self.id)

    def unlike(self):
        """
        Remove the Like of the connector
        """
        self.client._unlike(resource_id=self.id)


class Generator:
    OPEN_URL_PARTS: ClassVar[list] = ["d", "generators"]
    training: Annotated[Optional[Any], Field(exclude=True)] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.training = self.Training(self)

    def update(self, config) -> "Generator":
        """
        Update generator

        See config for the structure of the parameters.

        :return: The updated generator
        """
        return self.client._update(generator_id=self.id, config=config)

    def delete(self):
        """
        Delete generator
        """
        return self.client._delete(generator_id=self.id)

    def config(self) -> dict[str, Any]:
        """
        Retrieve writeable generator properties

        :return: The generator properties as dictionary
        """
        return self.client._config(generator_id=self.id)

    def export_to_file(
        self,
        file_path: Union[str, Path, None] = None,
    ) -> Path:
        """
        Export generator and save to file

        :param file_path: The file path to save the synthetic dataset
        """
        bytes, filename = self.client._export_to_file(generator_id=self.id)
        file_path = Path(file_path or ".")
        if file_path.is_dir():
            file_path = file_path / filename
        file_path.write_bytes(bytes)
        return file_path

    def clone(self, training_status: Literal["NEW", "CONTINUE"] = "NEW") -> "Generator":
        """
        Clone generator

        :param training_status: The training status of the cloned generator
        """
        return self.client._clone(generator_id=self.id, training_status=training_status)

    def shares(self):
        """
        Retrieve list of shares

        :return: list of ResourceShares
        """
        return self.client._list_shares(resource_id=self.id)

    def share(
        self, user_email: str, permission_level: PermissionLevel = PermissionLevel.view
    ):
        """
        Share the generator with specified user and access rights (default PermissionLevel.view)
        """
        self.client._share(
            resource_id=self.id,
            user_email=user_email,
            permission_level=permission_level,
        )

    def unshare(self, user_email: str):
        """
        Stop sharing the generator with the specified user
        """
        self.client._unshare(resource_id=self.id, user_email=user_email)

    def share_public(self):
        """
        Share the generator with everyone
        """
        self.client._share_public(resource_id=self.id)

    def unshare_public(self):
        """
        Stop sharing the generator with everyone
        """
        self.client._unshare_public(resource_id=self.id)

    def like(self):
        """
        Like the generator
        """
        self.client._like(resource_id=self.id)

    def unlike(self):
        """
        Remove the Like of the generator
        """
        self.client._unlike(resource_id=self.id)

    class Training:
        def __init__(self, _generator: "Generator"):
            self.generator = _generator

        def start(self) -> None:
            """
            Start training
            """
            return self.generator.client._training_start(self.generator.id)

        def cancel(self) -> None:
            """
            Cancel training
            """
            return self.generator.client._training_cancel(self.generator.id)

        def progress(self) -> JobProgress:
            """
            Retrieve job progress of training
            """
            return self.generator.client._training_progress(self.generator.id)

        def wait(self, progress_bar: bool, interval: float = 2) -> "Generator":
            """
            Poll training progress and loop until training has completed

            :param progress_bar: If true, then the progress bar will be displayed.
            :param interval: The interval in seconds to poll the job progress
            """
            return self.generator.client._training_wait(
                self.generator.id, progress_bar=progress_bar, interval=interval
            )

        def list_synthetic_dataset(self) -> list["SyntheticDataset"]:
            """
            List synthetic datasets

            List the synthetic datasets that were created based on this generator.

            :return: A list of synthetic datasets
            """
            raise "Not implemented yet."
            # return self.generator.client._list_synthetic_datasets(self.generator.id)
            pass


class SyntheticDataset:
    OPEN_URL_PARTS: ClassVar[list] = ["d", "synthetic-datasets"]
    generation: Annotated[Optional[Any], Field(exclude=True)] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generation = self.Generation(self)

    def update(self, config) -> "SyntheticDataset":
        """
        Update synthetic dataset

        See config for the structure of the parameters.

        :return: The updated synthetic dataset
        """
        return self.client._update(synthetic_dataset_id=self.id, config=config)

    def delete(self):
        """
        Delete synthetic dataset
        """
        return self.client._delete(synthetic_dataset_id=self.id)

    def config(self) -> dict[str, Any]:
        """
        Retrieve writeable synthetic dataset properties

        :return: The synthetic dataset properties as dictionary
        """
        return self.client._config(synthetic_dataset_id=self.id)

    def download(
        self,
        format: SyntheticDatasetFormat = "PARQUET",
        file_path: Union[str, Path, None] = None,
    ) -> Path:
        """
        Download synthetic dataset and save to file

        :param format: The format of the synthetic dataset
        :param file_path: The file path to save the synthetic dataset
        """
        bytes, filename = self.client._download(
            synthetic_dataset_id=self.id,
            ds_format=format,
            short_lived_file_token=self.metadata.short_lived_file_token,
        )
        file_path = Path(file_path or ".")
        if file_path.is_dir():
            file_path = file_path / filename
        file_path.write_bytes(bytes)
        return file_path

    def data(
        self, return_type: Literal["auto", "dict"] = "auto"
    ) -> Union[pd.DataFrame, dict[str, pd.DataFrame]]:
        """
        Download synthetic dataset and return as dictionary of pandas DataFrames

        :return: The synthetic dataset as dictionary of pandas DataFrames
        """
        dfs = self.client._data(
            synthetic_dataset_id=self.id,
            short_lived_file_token=self.metadata.short_lived_file_token,
        )
        if return_type == "auto" and len(dfs) == 1:
            return list(dfs.values())[0]
        else:
            return dfs

    def shares(self):
        """
        Retrieve list of shares

        :return: list of ResourceShares
        """
        return self.client._list_shares(resource_id=self.id)

    def share(
        self, user_email: str, permission_level: PermissionLevel = PermissionLevel.view
    ):
        """
        Share the Synthetic Data with specified user and access rights (default PermissionLevel.view)
        """
        self.client._share(
            resource_id=self.id,
            user_email=user_email,
            permission_level=permission_level,
        )

    def unshare(self, user_email: str):
        """
        Stop sharing the Synthetic Data with the specified user
        """
        self.client._unshare(resource_id=self.id, user_email=user_email)

    def share_public(self):
        """
        Share the Synthetic Data with everyone
        """
        self.client._share_public(resource_id=self.id)

    def unshare_public(self):
        """
        Stop sharing the Synthetic Data with everyone
        """
        self.client._unshare_public(resource_id=self.id)

    def like(self):
        """
        Like the Synthetic Data
        """
        self.client._like(resource_id=self.id)

    def unlike(self):
        """
        Remove the Like of the Synthetic Data
        """
        self.client._unlike(resource_id=self.id)

    class Generation:
        def __init__(self, _synthetic_dataset: "SyntheticDataset"):
            self.synthetic_dataset = _synthetic_dataset

        def start(self) -> None:
            """
            Start generation
            """
            return self.synthetic_dataset.client._generation_start(
                self.synthetic_dataset.id
            )

        def cancel(self) -> None:
            """
            Cancel generation
            """
            return self.synthetic_dataset.client._generation_cancel(
                self.synthetic_dataset.id
            )

        def progress(self) -> JobProgress:
            """
            Retrieve job progress of generation
            """
            return self.synthetic_dataset.client._generation_progress(
                self.synthetic_dataset.id
            )

        def wait(self, progress_bar: bool, interval: float = 2) -> "SyntheticDataset":
            """
            Poll generation progress and loop until generation has completed

            :param progress_bar: If true, then the progress bar will be displayed.
            :param interval: The interval in seconds to poll the job progress
            """
            return self.synthetic_dataset.client._generation_wait(
                self.synthetic_dataset.id, progress_bar=progress_bar, interval=interval
            )
