import allure
import pytest
from endpoints.accounts_endpoint import AccountsEndpoint


@allure.feature("Accounts API")
@allure.story("Retrieve Account List")
@pytest.mark.api
@pytest.mark.smoke
class TestAccountsAPI:
    def test_get_accounts_list(self, customer_id):
        accounts_endpoint = AccountsEndpoint()
        accounts_endpoint.get_accounts_list(customer_id)
        accounts_endpoint.check_response_is_200()
        accounts_endpoint.check_response_has_accounts()
        accounts_endpoint.check_accounts_fields()