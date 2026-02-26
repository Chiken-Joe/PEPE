class BookingAsserts:
    @staticmethod
    def assert_booking_equals(actual_json, expected_subset):
        for key, value in expected_subset.items():
            if key == "bookingdates":
                assert actual_json.get(key) == value, f"Bookingdates mismatch: expected {value}, got {actual_json.get(key)}"
            else:
                assert actual_json.get(key) == value, f"Field '{key}' mismatch: expected {value}, got {actual_json.get(key)}"