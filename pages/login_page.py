from utils.read_config import AppConfiguration
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    class _Selectors:
        USERNAME_FIELD = ".input[name='username']"
        PASSWORD_FIELD = ".input[name='password']"
        LOGIN_BUTTON  = ".button[value='Log In']"
        ERROR_MSG = ".error"
        TRANSFER_FUNDS_LINK = "Transfer Funds"


    def __init__(self, page):
        super().__init__(page)

    def login_page_open(self):
        self.navigate_to(AppConfiguration.get_common_info()["Url"])  # From config.json

    def enter_valid_username(self):
        common_info = AppConfiguration.get_common_info()
        self.wait_and_fill(self.page.locator(self._Selectors.USERNAME_FIELD), common_info["UserName"])

    def enter_valid_password(self):
        common_info = AppConfiguration.get_common_info()
        self.wait_and_fill(self.page.locator(self._Selectors.PASSWORD_FIELD), common_info["Password"])

    def enter_invalid_username(self):
        self.wait_and_fill(self.page.locator(self._Selectors.USERNAME_FIELD), "wrongUser")
    #  for this site only empty fields can call error message, if enters any char site logged user in
    def enter_invalid_password(self):
        self.wait_and_fill(self.page.locator(self._Selectors.PASSWORD_FIELD), "")

    def click_login_button(self):
        self.wait_and_click(self.page.locator(self._Selectors.LOGIN_BUTTON))

    def error_message_displayed(self):
        expect(self.page.locator(self._Selectors.ERROR_MSG)).to_be_visible()

    def enter_valid_credentials_and_click_login_button(self):
        self.enter_valid_username()
        self.enter_valid_password()
        self.click_login_button()

    def click_transfer_funds_page_link(self):
        self.wait_and_click(self.page.get_by_role("link", name=self._Selectors.TRANSFER_FUNDS_LINK))