from api.base_client import BaseClient
from typing import Optional, Dict, Any

class BookingClient(BaseClient):
    def get_booking_ids(self, params: Optional[Dict] = None):
        return self._request("GET", "/booking", params=params)

    def get_booking(self, booking_id: int):
        return self._request("GET", f"/booking/{booking_id}")

    def create_booking(self, payload: Dict[str, Any]):
        return self._request("POST", "/booking", json=payload)

    def update_booking(self, booking_id: int, payload: Dict[str, Any]):
        return self._request("PUT", f"/booking/{booking_id}", json=payload)

    def partial_update_booking(self, booking_id: int, payload: Dict[str, Any]):
        return self._request("PATCH", f"/booking/{booking_id}", json=payload)

    def delete_booking(self, booking_id: int):
        return self._request("DELETE", f"/booking/{booking_id}")