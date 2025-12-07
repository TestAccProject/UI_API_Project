import xml.etree.ElementTree as ET
from endpoints.base_endpoint import Endpoint


class CustomersEndpoint(Endpoint):
    def get_customer(self, customer_id):
        response = self.client.get(f"customers/{customer_id}")
        self.response = response

        root = ET.fromstring(response.text)
        self.response_json = {}
        for child in root:
            if child.tag == "address":
                self.response_json["address"] = {grandchild.tag: grandchild.text for grandchild in child}
            else:
                self.response_json[child.tag] = child.text

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def check_response_id(self, customer_id):
        assert self.response_json["id"] == "12212"

    def check_response_fields(self, expected_fields: dict):
        for field, expected_value in expected_fields.items():
            assert self.response_json[field] == expected_value