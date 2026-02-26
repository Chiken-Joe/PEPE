import pytest

from api.booking_client import BookingClient
from asserts.response_asserts import ResponseAsserts as RA
from asserts.booking_asserts import BookingAsserts as BA
from fixtures.booking_factory import valid_booking_payload
from tests.conftest import booking_client


#test-1
def test_ping(auth_client):
    client = BookingClient()
    response = client._request("GET", "/ping")
    RA.assert_status(response, 201)
    assert response.text == "Created"

#test-2
def test_auth_success(auth_client):
    response = auth_client.create_token()
    RA.assert_status(response, 200)
    RA.assert_json_has_keys(response.json(), ["token"])

#test-4
def test_get_all_booking_ids(booking_client):
    response = booking_client.get_booking_ids()
    RA.assert_status(response, 200)
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "bookingid" in data[0]

#test-10
def test_create_booking(booking_client):
    payload = valid_booking_payload()
    response = booking_client.create_booking(payload)
    RA.assert_status(response, 200)
    json_data = response.json()
    RA.assert_json_has_keys(json_data, ["bookingid", "booking"])
    BA.assert_booking_equals(json_data["booking"], payload)

#test-11
def test_create_booking_unauth(unauth_booking_client):
    payload = valid_booking_payload()
    response = unauth_booking_client.create_booking(payload)
    RA.assert_status(response, 200)
    json_data = response.json()
    RA.assert_json_has_keys(json_data, ["bookingid", "booking"])
    BA.assert_booking_equals(json_data["booking"], payload)

#test-8
def test_get_booking_by_id(booking_client, create_booking):
    create_resp = create_booking()
    RA.assert_status(create_resp, 200)
    booking_id = create_resp.json()["bookingid"]
    response = booking_client.get_booking(booking_id)
    RA.assert_status(response, 200)
    json_data = response.json()
    RA.assert_json_has_keys(json_data, ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"])

#test-15
def test_full_update_booking(booking_client, create_booking):
    create_resp = create_booking()
    booking_id = create_resp.json()["bookingid"]
    updated_payload = valid_booking_payload()
    updated_payload["firstname"] = "Jane"
    updated_payload["lastname"] = "Doe"
    response = booking_client.update_booking(booking_id, updated_payload)
    RA.assert_status(response, 200)
    BA.assert_booking_equals(response.json(), updated_payload)

#test-16
def test_full_update_booking_unauth(unauth_booking_client, create_booking):
    create_resp = create_booking()
    booking_id = create_resp.json()["bookingid"]
    updated_payload = valid_booking_payload()
    response = unauth_booking_client.update_booking(booking_id, updated_payload)
    RA.assert_status(response, 403)

#test-17
def test_partial_update_booking(booking_client, create_booking):
    create_resp = create_booking()
    booking_id = create_resp.json()["bookingid"]
    get_resp = booking_client.get_booking(booking_id)
    original_data = get_resp.json()
    patch_payload = {"firstname": "Patched"}
    response = booking_client.partial_update_booking(booking_id, patch_payload)
    RA.assert_status(response, 200)
    patched_data = response.json()
    assert patched_data["firstname"] == "Patched"
    assert patched_data["lastname"] == original_data["lastname"]
    assert patched_data["totalprice"] == original_data["totalprice"]

#test-18
def test_delete_booking(booking_client, create_booking):
    create_resp = create_booking()
    booking_id = create_resp.json()["bookingid"]
    response = booking_client.delete_booking(booking_id)
    RA.assert_status(response, 201)
    get_resp = booking_client.get_booking(booking_id)
    RA.assert_status(get_resp, 404)

#test-20
def test_delete_booking_unauth(unauth_booking_client, booking_client, create_booking):
    create_resp = create_booking()
    booking_id = create_resp.json()["bookingid"]
    response = unauth_booking_client.delete_booking(booking_id)
    RA.assert_status(response, 403)
    get_resp = booking_client.get_booking(booking_id)
    RA.assert_status(get_resp, 200)