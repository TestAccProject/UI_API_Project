import allure
import pytest
from endpoints.negative_endpoint import NegativeEndpoint


@allure.feature("Accounts API")
@allure.story("Negative: Invalid Account ID")
@pytest.mark.api
@pytest.mark.smoke
class TestNegativeAPI:
    def test_negative_invalid_customer_accounts(self, customer_id):
        negative_endpoint = NegativeEndpoint()
        negative_endpoint.negative_invalid_customer_accounts(customer_id)
        negative_endpoint.check_response_is_404()