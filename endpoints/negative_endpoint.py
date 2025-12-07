import requests
from requests.auth import HTTPBasicAuth
from utils.read_config import AppConfiguration


class NegativeEndpoint:
    def __init__(self):
        common_info = AppConfiguration.get_common_info()
        self.base_url = common_info.get("BaseApiUrl", "https://parabank.parasoft.com/parabank/services/bank")
        self.username = common_info.get("UserName", "john")
        self.password = common_info.get("Password", "")
        self.auth = HTTPBasicAuth(self.username, self.password)

    def negative_invalid_customer_accounts(self, customer_id: int, invalid_account_id: int = 12212000000):
        """GET /customers/{customer_id}/accounts/{invalid_account_id} (expects 404)."""
        url = f"{self.base_url}/customers/{customer_id}/accounts/{invalid_account_id}"
        self.response = requests.get(url, auth=self.auth)
        self.response_text = self.response.text.strip()
        return self.response

    def check_response_is_404(self):
        assert self.response.status_code == 404, f"Expected 404, got {self.response.status_code}"

    def check_error_message(self, expected_phrase: str = "not found"):
        assert expected_phrase in self.response_text.lower(), f"Expected '{expected_phrase}', got: {self.response_text}"