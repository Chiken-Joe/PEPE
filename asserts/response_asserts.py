class ResponseAsserts:
    @staticmethod
    def assert_status(response, expected_status):
        assert response.status_code == expected_status, \
            f"Expected status {expected_status}, got {response.status_code}"

    @staticmethod
    def assert_json_has_keys(json_data, expected_keys):
        for key in expected_keys:
            assert key in json_data, f"Key '{key}' not found in response JSON"

    @staticmethod
    def assert_error_message(response, expected_message):
        json_data = response.json()
        assert json_data.get("reason") == expected_message, \
            f"Expected error message '{expected_message}', got '{json_data.get('reason')}'"