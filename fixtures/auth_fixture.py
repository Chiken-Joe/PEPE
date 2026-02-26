import pytest
from api.auth_client import AuthClient

@pytest.fixture(scope="session")
def auth_token():
    client = AuthClient()
    response = client.create_token()
    assert response.status_code == 200, "Failed to get auth token"
    token = response.json().get("token")
    assert token, "Token not found in response"
    return token