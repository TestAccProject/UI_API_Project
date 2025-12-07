import allure
import pytest
from pages.account_overview_page import AccountOverviewPage
from tests.test_ui.test_base import BaseTest
from pages.login_page import LoginPage
from playwright.sync_api import Page
from utils.read_config import AppConfiguration

@allure.feature("Login Page")
@allure.story("Login Functionality")
@pytest.mark.smoke
class TestLogin(BaseTest):
    @allure.title("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_user_login(self, page:Page):
        common_info = AppConfiguration.get_common_info()
        login_page = LoginPage(page)
        account_overview_page = AccountOverviewPage(page)
        login_page.login_page_open()
        login_page.enter_valid_username()
        login_page.enter_valid_password()
        login_page.click_login_button()
        account_overview_page.check_welcome_message()


    @allure.title("Error Message Is Displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_username_login(self, page: Page):
        login_page = LoginPage(page)
        login_page.login_page_open()
        login_page.enter_invalid_username()
        login_page.enter_invalid_password()
        login_page.click_login_button()
        login_page.error_message_displayed()


