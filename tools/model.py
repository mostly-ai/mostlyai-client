from typing import Optional, Annotated, Any

import pandas as pd
from pydantic import Field


class Connector:
    def config(self):
        if self.client and hasattr(self.client, "config"):
            return self.client.config(connector_id=self.id)

    def update(self, **kwargs):
        if self.client and hasattr(self.client, "update"):
            return self.client.update(connector_id=self.id, **kwargs)

    def delete(self):
        if self.client and hasattr(self.client, "delete"):
            return self.client.delete(connector_id=self.id)

    def locations(self, prefix: str = "") -> list:
        """Retrieve the locations associated with this connector and prefix.

        :param prefix: A prefix to filter the locations, defaults to "".
        :return: A list of locations (schemas, databases, directories, etc.) on the
            given level.
        """
        if self.client and hasattr(self.client, "locations"):
            return self.client.locations(connector_id=self.id, prefix=prefix)


class Generator:
    training: Annotated[Optional[Any], Field(exclude=True)] = None

    class Training:
        def __init__(self, _generator: "Generator"):
            self.generator = _generator

        def progress(self):
            self.generator.client.get_training_progress(self.generator.id)

        def start(self):
            self.generator.client.start_training(self.generator.id)

        def stop(self):
            self.generator.client.stop_training(self.generator.id)

        def cancel(self):
            self.generator.client.cancel_training(self.generator.id)

        def wait(self, interval: float = 5):
            # block until training is done
            # poll every {interval} seconds
            self.generator.client.training_wait(self.generator.id, interval=interval)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.training = self.Training(self)

    def add_table(
        self,
        sourceConnectorId: str,
        location: str,
        name: Optional[str] = None,
        includeChildren: Optional[bool] = False,
        modelConfiguration: Optional["ModelConfiguration"] = None,
        textModelConfiguration: Optional["ModelConfiguration"] = None,
    ) -> "SourceTable":
        """Add table to generator.

        :param sourceConnectorId: The unique identifier of a connector
        :param location: The location of a source table
        :param name: The name of a source table
        :param includeChildren: If true, all tables that are referenced by foreign keys
            will be included. If false, only the selected table will be included.
        :param modelConfiguration:
        :param textModelConfiguration:
        :return: The added source table object
        """
        params = {
            "sourceConnectorId": sourceConnectorId,
            "location": location,
            "name": name,
            "includeChildren": includeChildren,
            "modelConfiguration": modelConfiguration,
            "textModelConfiguration": textModelConfiguration,
        }
        if self.client and hasattr(self.client, "add_table"):
            return self.client.add_table(generator_id=self.id, **params)

    def add_table_by_upload(
        self,
        file: str,
        name: Optional[str] = None,
        primaryKey: Optional[str] = None,
        modelConfiguration: Optional["ModelConfiguration"] = None,
        textModelConfiguration: Optional["ModelConfiguration"] = None,
    ) -> "SourceTable":
        """Add table to generator by uploading a data file.

        :param file: Path to the file to upload
        :param name: The name of a source table
        :param includeChildren: If true, all tables that are referenced by foreign keys
            will be included. If false, only the selected table will be included.
        :param modelConfiguration:
        :param textModelConfiguration:
        :return: The added source table object
        """
        params = {
            "file": file,
            "name": name,
            "primaryKey": primaryKey,
            "modelConfiguration": modelConfiguration,
            "textModelConfiguration": textModelConfiguration,
        }
        if self.client and hasattr(self.client, "add_table_by_upload"):
            return self.client.add_table_by_upload(generator_id=self.id, **params)

    def add_table_from_df_by_upload(
        self,
        df: pd.DataFrame,
        name: Optional[str] = None,
        primaryKey: Optional[str] = None,
        modelConfiguration: Optional["ModelConfiguration"] = None,
        textModelConfiguration: Optional["ModelConfiguration"] = None,
    ) -> "SourceTable":
        """Add table to generator from a pd.DataFrame object.

        :param df: DataFrame that represents the table to be added
        :param name: The name of a source table
        :param includeChildren: If true, all tables that are referenced by foreign keys
            will be included. If false, only the selected table will be included.
        :param modelConfiguration:
        :param textModelConfiguration:
        :return: The added source table object
        """
        if self.client and hasattr(self.client, "add_table_from_df_by_upload"):
            params = {
                "df": df,
                "name": name,
                "primaryKey": primaryKey,
                "modelConfiguration": modelConfiguration,
                "textModelConfiguration": textModelConfiguration,
            }
            return self.client.add_table_from_df_by_upload(
                generator_id=self.id, **params
            )

    def get_table(self, table_id: str) -> "SourceTable":
        if self.client and hasattr(self.client, "get_table"):
            return self.client.get_table(generator_id=self.id, table_id=table_id)

    def update_table(self, **kwargs) -> "SourceTable":
        if self.client and hasattr(self.client, "update_table"):
            return self.client.update_table(generator_id=self.id, **kwargs)

    def delete_table(self, **kwargs) -> "SourceTable":
        if self.client and hasattr(self.client, "delete_table"):
            return self.client.delete_table(generator_id=self.id, **kwargs)


class SourceTable:
    def model_qa_report(self) -> "ModelQAReport":
        if self.client and hasattr(self.client, "model_qa_report"):
            return self.client.model_qa_report(
                generator_id=self.extra_key_values["generator_id"], table_id=self.id
            )

    def model_samples(self, **kwargs):
        if self.client and hasattr(self.client, "model_samples"):
            return self.client.model_qa_report(
                generator_id=self.extra_key_values["generator_id"],
                table_id=self.id,
                **kwargs
            )

    def get_column(self, column_id: str):
        if self.client and hasattr(self.client, "get_column"):
            return self.client.get_column(
                generator_id=self.extra_key_values["generator_id"],
                table_id=self.id,
                column_id=column_id,
            )

    def create_foreign_key(self, **kwargs):
        if self.client and hasattr(self.client, "create_foreign_key"):
            return self.client.create_foreign_key(
                generator_id=self.extra_key_values["generator_id"],
                table_id=self.id,
                **kwargs
            )

    def update_foreign_key(self, **kwargs):
        if self.client and hasattr(self.client, "update_foreign_key"):
            return self.client.update_foreign_key(
                generator_id=self.extra_key_values["generator_id"],
                table_id=self.id,
                **kwargs
            )

    def delete_foreign_key(self, **kwargs):
        if self.client and hasattr(self.client, "delete_foreign_key"):
            return self.client.delete_foreign_key(
                generator_id=self.extra_key_values["generator_id"],
                table_id=self.id,
                **kwargs
            )