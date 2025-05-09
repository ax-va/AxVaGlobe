import pytest

from core.schema.schema import Schema


@pytest.fixture(scope="session")
def schema_two(tmp_path_factory):
    return Schema(2)


@pytest.fixture(scope="session")
def schema_three(tmp_path_factory):
    return Schema(3)


@pytest.fixture(scope="session")
def schema_four(tmp_path_factory):
    return Schema(4)


@pytest.fixture(scope="session")
def schema_five(tmp_path_factory):
    return Schema(5)
