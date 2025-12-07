import xml.etree.ElementTree as ET
from endpoints.base_endpoint import Endpoint


class AccountsEndpoint(Endpoint):
    def get_accounts_list(self, customer_id):
        response = self.client.get(f"customers/{customer_id}/accounts")
        self.response = response

        root = ET.fromstring(response.text)
        accounts = []
        for account_elem in root.findall("account"):
            account = {}
            for child in account_elem:
                account[child.tag] = child.text
            accounts.append(account)

        self.response_json = accounts
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_has_accounts(self):
        accounts = self.response_json
        assert len(accounts) > 0, f"Expected non-empty accounts, got {len(accounts)}"

    def check_accounts_fields(self):
        accounts = self.response_json
        for account in accounts:
            assert "id" in account
            assert int(account["id"])
            assert "type" in account and isinstance(account["type"], str)
            assert "balance" in account and isinstance(float(account["balance"]), (int, float))