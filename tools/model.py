class Connector:
    def locations(self, prefix: str = "") -> list:
        if self.client and hasattr(self.client, "locations"):
            return self.client.locations(connector_id=self.id, prefix=prefix)


class Generator:
    def add_table(self, **kwargs) -> "Table":
        if self.client and hasattr(self.client, "add_table"):
            return self.client.add_table(generator_id=self.id, **kwargs)

    def add_table_by_upload(self, **kwargs) -> "Table":
        if self.client and hasattr(self.client, "add_table_by_upload"):
            return self.client.add_table_by_upload(generator_id=self.id, **kwargs)

    def add_table_from_df_by_upload(self, **kwargs) -> "Table":
        if self.client and hasattr(self.client, "add_table_from_df_by_upload"):
            return self.client.add_table_from_df_by_upload(
                generator_id=self.id, **kwargs
            )

    def get_table(self, **kwargs) -> "Table":
        if self.client and hasattr(self.client, "get_table"):
            return self.client.get_table(generator_id=self.id, **kwargs)

    def update_table(self, **kwargs) -> "Table":
        if self.client and hasattr(self.client, "update_table"):
            return self.client.update_table(generator_id=self.id, **kwargs)

    def delete_table(self, **kwargs) -> "Table":
        if self.client and hasattr(self.client, "delete_table"):
            return self.client.delete_table(generator_id=self.id, **kwargs)
