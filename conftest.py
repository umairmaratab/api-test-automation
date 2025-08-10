import pytest
from utils.api_client import APIClient
from dotenv import dotenv_values

@pytest.fixture(scope="session")
def config():
    # loads from .env if present (optional), otherwise fallback to config/config.yaml in APIClient
    return dotenv_values('.env')

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def created_user(api_client):
    """
    Create a test user and yield the created resource (response json).
    Note: ReqRes is a mock API and does not persist user data long-term, but it returns a created id.
    """
    payload = {"name": "temp-user", "job": "tester"}
    r = api_client.post("/users", json=payload)
    assert r.status_code in (201, 200)
    data = r.json()
    yield data
    # cleanup step omitted because ReqRes does not persist resources reliably
