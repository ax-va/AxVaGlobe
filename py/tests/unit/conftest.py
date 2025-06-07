def pytest_collection_modifyitems(items):
    """
    This pytest hook function applies the "unit" marker to all tests in the directory and its subdirectories.
    This equivalent to decorating each function with `@pytest.mark.unit` or
    adding `pytestmark = pytest.mark.unit` to each module.
    """
    for item in items:
        item.add_marker("unit")
