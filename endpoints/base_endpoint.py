import logging
from utils.api_client import APIClient



logger = logging.getLogger(__name__)


class Endpoint:
    def __init__(self):
        self.client = APIClient()  # Shared HTTP client with auth/config
        self.response = None
        self.response_json = None

    def _handle_response(self, response):
        self.response = response
        if response.ok:
            self.response_json = response.json()  # Assume JSON; add XML fallback if needed
            logger.info(f"Response OK: {response.status_code} - Parsed JSON")
        else:
            logger.error(f"Response failed: {response.status_code} - {response.text}")
            response.raise_for_status()  # Raises on 4xx/5xx
        return self.response

    def check_response_is_200(self):
        assert self.response.status_code == 200, f"Expected 200, got {self.response.status_code}"

    def check_response_is_404(self):
        assert self.response.status_code == 404, f"Expected 404, got {self.response.status_code}"

    def check_response_is_json(self):
        assert self.response_json is not None, "Expected JSON response, got None"

    def check_response_id(self, expected_id: int):
        """Assert response ID matches expected."""
        self.check_response_is_json()
        assert self.response_json["id"] == expected_id, f"Expected ID {expected_id}, got {self.response_json.get('id')}"

    def check_response_fields(self, expected_fields: dict):
        """Assert specific fields match expected values."""
        self.check_response_is_json()
        for field, expected_value in expected_fields.items():
            assert self.response_json[field] == expected_value, f"Expected {field} = {expected_value}, got {self.response_json.get(field)}"
