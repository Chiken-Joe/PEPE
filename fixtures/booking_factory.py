import pytest
from api.booking_client import BookingClient

def valid_booking_payload():
    return {
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Breakfast"
    }

def invalid_booking_payload():
    return {
        "lastname": "Smith",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        }
    }

@pytest.fixture
def create_booking(auth_token):
    client = BookingClient()
    client.set_auth_cookie(auth_token)
    def _make(payload=None):
        if payload is None:
            payload = valid_booking_payload()
        response = client.create_booking(payload)
        return response
    return _make