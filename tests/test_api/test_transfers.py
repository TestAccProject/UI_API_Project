import allure
import pytest
from endpoints.transfers_endpoint import TransfersEndpoint


@allure.feature("Transfers API")
@allure.story("Create Transfer Resource")
@pytest.mark.api
@pytest.mark.smoke
class TestSimpleTransfersAPI:
    def test_create_transfer(self, customer_id):
        create_transfer = TransfersEndpoint()
        create_transfer.create_transfer()