import pytest
from api.auth_client import AuthClient
from api.booking_client import BookingClient
from fixtures.auth_fixture import auth_token
from fixtures.booking_factory import create_booking, valid_booking_payload, invalid_booking_payload

@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def booking_client(auth_token):
    client = BookingClient()
    client.set_auth_cookie(auth_token)
    return client

@pytest.fixture
def unauth_booking_client():
    return BookingClient()