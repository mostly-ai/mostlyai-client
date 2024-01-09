import pytest

from mostlyai.exceptions import APIStatusError
from mostlyai.model import Generator, SourceTable


@pytest.fixture
def new_generator_params():
    return {
        "name": "Test Generator",
    }


class TestGenerators:
    def test_list(self, mostly_client):
        for generator in mostly_client.generators.list():
            assert isinstance(generator, Generator)

    def test_create_get_update_delete(self, mostly_client, new_generator_params):
        generator = mostly_client.generators.create(**new_generator_params)
        assert isinstance(generator, Generator)

        generator_id = str(generator.id)
        generator = mostly_client.generators.get(generator_id)
        assert str(generator.id) == generator_id

        updated_params = {"name": "Updated Test Generator"}
        # TODO ensure that this works
        updated_generator = mostly_client.generators.update(
            generator_id, **updated_params
        )
        assert updated_generator.name == "Updated Test Generator"

        mostly_client.generators.delete(generator_id)

    def test_add_get_update_delete_table(
        self, mostly_client, new_generator_params, local_connector
    ):
        generator = mostly_client.generators.create(**new_generator_params)

        # TODO ensure that this works
        new_table = generator.add_table(
            sourceConnectorId=str(local_connector.id), location=""
        )
        table = generator.get_table(new_table.id)
        generator.update_table(table.id)
        generator.delete_table(table.id)
