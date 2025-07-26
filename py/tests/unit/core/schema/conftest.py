import pytest

from core.schema.schema import Schema


@pytest.fixture(scope="function")
def schema_two():
    return Schema(2)


@pytest.fixture(scope="function")
def schema_three():
    return Schema(3)


@pytest.fixture(scope="function")
def schema_four():
    return Schema(4)


@pytest.fixture(scope="function")
def schema_five():
    return Schema(5)
