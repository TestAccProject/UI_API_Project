import allure
import pytest
from endpoints.customers_endpoint import CustomersEndpoint


@allure.feature("Customers API")
@allure.story("Retrieve Customer Information")
@pytest.mark.api
@pytest.mark.smoke
class TestSimpleCustomersAPI:
    def test_get_customer(self, customer_id):
        customers_endpoint = CustomersEndpoint()
        customers_endpoint.get_customer(customer_id)
        customers_endpoint.check_response_is_200()
        customers_endpoint.check_response_id(customer_id)
        customers_endpoint.check_response_fields({"firstName": "John", "lastName": "Smith"})

