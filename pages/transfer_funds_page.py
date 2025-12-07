from playwright.sync_api import expect
from pages.base_page import BasePage


class TransferFundsPage(BasePage):
    class _Selectors:
        AMOUNT_INPUT_FIELD = "#amount"
        FROM_ACCOUNT_DROPDOWN = "#fromAccountId"
        ACCOUNT_SELECTED_FROM = "73617"
        ACCOUNT_SELECTED_TO = "73506"
        TO_ACCOUNT_DROPDOWN = "#toAccountId"
        TRANSFER_BUTTON = "Transfer"
        SUCCESS_MSG = "$10.00 has been transferred"
        ACCOUNT_OVERVIEW_LINK = "Accounts Overview"


    def __init__(self, page):
        super().__init__(page)

    def enter_amount(self):
        self.wait_and_fill(self.page.locator(self._Selectors.AMOUNT_INPUT_FIELD), "10")

    def select_from_account(self, account_id: str):
        self.page.locator(self._Selectors.FROM_ACCOUNT_DROPDOWN).select_option(self._Selectors.ACCOUNT_SELECTED_FROM)

    def select_to_account(self):
        self.page.locator(self._Selectors.TO_ACCOUNT_DROPDOWN).select_option(self._Selectors.ACCOUNT_SELECTED_TO)

    def click_transfer_button(self):
        self.page.get_by_role("button", name=self._Selectors.TRANSFER_BUTTON).click()

    def perform_transfer(self):
        self.wait_and_fill(self.page.locator(self._Selectors.AMOUNT_INPUT_FIELD), "10")
        self.page.locator(self._Selectors.FROM_ACCOUNT_DROPDOWN).select_option(self._Selectors.ACCOUNT_SELECTED_FROM)
        self.page.locator(self._Selectors.TO_ACCOUNT_DROPDOWN).select_option(self._Selectors.ACCOUNT_SELECTED_TO)
        self.page.get_by_role("button", name=self._Selectors.TRANSFER_BUTTON).click()

    def verify_success_message(self):
         expect(self.page.get_by_text(self._Selectors.SUCCESS_MSG)).to_contain_text("10")

    def click_account_overview(self):
        self.page.get_by_role("link", name=self._Selectors.ACCOUNT_OVERVIEW_LINK).click()

