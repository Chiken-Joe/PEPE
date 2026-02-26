from api.base_client import BaseClient

class AuthClient(BaseClient):
    def create_token(self, username="admin", password="password123"):
        payload = {"username": username, "password": password}
        response = self._request("POST", "/auth", json=payload)
        return response

