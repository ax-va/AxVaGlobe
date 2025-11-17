import pytest

from axvaglobe.core.schema.schema import Schema


@pytest.fixture(scope="function")
def schema_two():
    return Schema.get_schema(2)


@pytest.fixture(scope="function")
def schema_three():
    return Schema.get_schema(3)


@pytest.fixture(scope="function")
def schema_four():
    return Schema.get_schema(4)


@pytest.fixture(scope="function")
def schema_five():
    return Schema.get_schema(5)
