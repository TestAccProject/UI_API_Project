import requests
from requests.auth import HTTPBasicAuth
from endpoints.base_endpoint import Endpoint  # Your base
from utils.read_config import AppConfiguration


class GetCustomer(Endpoint):
    def get_customer_details(self, customer_id: int = 12212):
        common_info = AppConfiguration.get_common_info()
        base_url = common_info.get("BaseApiUrl", "https://parabank.parasoft.com/parabank/services/bank")
        username = common_info.get("UserName", "john")
        password = common_info.get("Password", "")
        auth = HTTPBasicAuth(username, password)

        endpoint = f"customers/{customer_id}"
        url = f"{base_url}/{endpoint}"
        self.response = requests.get(url, auth=auth)

        self._handle_response(self.response)
        self.response_json = self.response.json()

    def check_response_fields(self):
        assert self.response_json["id"] == 12212
        assert self.response_json["firstName"] == "John"
        assert self.response_json["lastName"] == "Smith"
        assert self.response_json["phoneNumber"] == "310-447-4121"
        assert self.response_json["ssn"] == "622-11-9999"
        assert self.response_json["address"]["street"] == "1431 Main St"
        assert self.response_json["address"]["city"] == "Beverly Hills"
