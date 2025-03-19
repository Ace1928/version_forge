import pytest

@pytest.fixture(scope='session')
def sample_fixture():
    return "sample data"

@pytest.fixture
def another_fixture():
    return "another sample"

def pytest_configure():
    pytest.addoption("--verbose", action="store_true", help="Enable verbose output")
    
def pytest_collection_modifyitems(config, items):
    if config.getoption("--verbose"):
        for item in items:
            item.user_properties.append(("verbose", True))