from endpoints.base_endpoint import Endpoint
from requests.auth import HTTPBasicAuth
from utils.read_config import AppConfiguration
import requests


class TransfersEndpoint(Endpoint):
    def create_transfer(self, from_account_id=13344, to_account_id=15786, amount=10.00):
        common_info = AppConfiguration.get_common_info()
        base_url = common_info.get("BaseApiUrl", "https://parabank.parasoft.com/parabank/services/bank")
        username = common_info.get("UserName", "john")
        password = common_info.get("Password", "")
        auth = HTTPBasicAuth(username, password)

        endpoint = "transfer"
        url = f"{base_url}/{endpoint}"
        params = {
            "fromAccountId": from_account_id,
            "toAccountId": to_account_id,
            "amount": amount
        }
        self.response = requests.get(url, params=params, auth=auth)

        self.response_text = self.response.text.strip()

        assert self.response.status_code == 200, f"Expected 200, got {self.response.status_code}"
        expected_pattern = re.compile(
            r"Successfully transferred \${}\.00 from account #{} to account #{}".format(amount, from_account_id,
                                                                                        to_account_id), re.IGNORECASE)
        assert expected_pattern.search(self.response_text), f"Expected success msg, got: {self.response_text}"

        return self.response_text