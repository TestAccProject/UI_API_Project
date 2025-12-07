from playwright.sync_api import expect
from pages.base_page import BasePage
from utils.read_config import AppConfiguration


class AccountDetailsPage(BasePage):
    class _Selectors:
        ACCOUNT_NUMBER = "td[id='accountId']"
        BALANCE = "td[id='balance']"
        ACCOUNT_TYPE = "td[id='accountType']"
        TRANSACTIONS_TABLE = "table[id='transactionTable']"


    def __init__(self, page):
        super().__init__(page)

    def open_account_details_page(self):
        pass

    def account_number_verify(self):
        common_info = AppConfiguration.get_common_info()
        expect(self.page.locator(self._Selectors.ACCOUNT_NUMBER)).to_contain_text(common_info["AccountNumber"])

    def balance_verify(self):
        common_info = AppConfiguration.get_common_info()
        expect(self.page.locator(self._Selectors.BALANCE)).to_contain_text(common_info["Balance"])

    def account_type_verify(self):
        common_info = AppConfiguration.get_common_info()
        expect(self.page.locator(self._Selectors.ACCOUNT_TYPE)).to_contain_text(common_info["AccountType"])

    def transactions_table_is_displayed(self):
        expect(self.page.locator(self._Selectors.ACCOUNT_NUMBER)).to_be_visible()