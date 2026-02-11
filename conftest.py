import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
