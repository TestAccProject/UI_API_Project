import requests
import xml.etree.ElementTree as ET
from endpoints.base_endpoint import Endpoint
from utils.read_config import AppConfiguration


class LoginEndpoint(Endpoint):
    def login(self, username: str = None, password: str = None):
        common_info = AppConfiguration.get_common_info()
        username = username or common_info.get("UserName", "john")
        password = password or common_info.get("Password", "demo")

        endpoint = f"login/{username}/{password}"
        response = self.client.get(endpoint)

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"Login failed: {response.status_code} - {response.text}")

        root = ET.fromstring(response.text)
        customer_data = {}
        for child in root:
            if child.tag == "address":
                customer_data["address"] = {grandchild.tag: grandchild.text for grandchild in child}
            else:
                customer_data[child.tag] = child.text

        self.response_json = customer_data
        customer_id = int(customer_data.get("id"))
        assert customer_id is not None, f"Login failed—no customerId in XML: {customer_data}"
        return customer_id