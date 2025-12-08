import pytest
import allure
from pages.account_overview_page import AccountOverviewPage
from tests.test_ui.test_base import BaseTest
from pages.login_page import LoginPage
from playwright.sync_api import Page
from pages.transfer_funds_page import TransferFundsPage



@allure.feature("Transfer funds between own accounts")
@allure.story("User should be able to transfer funds between own accounts")
@pytest.mark.ui
@pytest.mark.smoke
class TestTransfer(BaseTest):

    @allure.title("E2E Transfer funds between own accounts")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_account_list_is_displayed(self, page: Page):
        login_page = LoginPage(page)
        transfer_funds_page = TransferFundsPage(page)
        account_overview_page = AccountOverviewPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        login_page.click_transfer_funds_page_link()
        transfer_funds_page.perform_transfer()
        transfer_funds_page.verify_success_message()
        transfer_funds_page.click_account_overview()
        account_overview_page.verify_account_balance()


