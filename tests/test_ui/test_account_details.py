import pytest
import allure
from pages.account_details_page import AccountDetailsPage
from pages.account_overview_page import AccountOverviewPage
from tests.test_ui.test_base import BaseTest
from pages.login_page import LoginPage
from playwright.sync_api import Page



@allure.feature("Account Overview")
@allure.story("Account Number Is Verified")
@pytest.mark.ui
@pytest.mark.smoke
class TestAccountOverview(BaseTest):

    @allure.title("Chek welcome message")
    @allure.severity(allure.severity_level.NORMAL)
    def test_account_list_is_displayed(self, page: Page):
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        account_details_page = AccountDetailsPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        account_overview_page.check_welcome_message()


    @allure.title("Account list is displayed")
    @allure.severity(allure.severity_level.NORMAL)
    def test_account_list_is_displayed(self, page: Page):
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        # account_details_page = AccountDetailsPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        account_overview_page.check_welcome_message()
        # account_overview_page.click_account_number()
        account_overview_page.account_number_verify()

    @allure.title("Account number verification")
    @allure.severity(allure.severity_level.NORMAL)
    def test_account_number_verification(self, page: Page):
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        account_details_page = AccountDetailsPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        account_overview_page.click_account_number()
        account_details_page.account_number_verify()


    @allure.title("Balance verification")
    @allure.severity(allure.severity_level.NORMAL)
    def test_balance_verification(self, page: Page):
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        account_details_page = AccountDetailsPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        account_overview_page.click_account_number()
        account_details_page.balance_verify()

    @allure.title("Account type verification")
    @allure.severity(allure.severity_level.NORMAL)
    def test_account_type_verification(self, page: Page):
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        account_details_page = AccountDetailsPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        account_overview_page.click_account_number()
        account_details_page.account_type_verify()

    @allure.title("Transaction table is displayed")
    @allure.severity(allure.severity_level.NORMAL)
    def test_transaction_table_is_displayed(self, page: Page):
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        account_details_page = AccountDetailsPage(page)
        login_page.login_page_open()
        login_page.enter_valid_credentials_and_click_login_button()
        account_overview_page.click_account_number()
        account_details_page.transactions_table_is_displayed()