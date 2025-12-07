import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from utils.read_config import AppConfiguration


class AccountOverviewPage(BasePage):
    class _Selectors:
        WELCOME_MSG = "Welcome John Smith"
        ACCOUNT_NUMBER_LINK = "12345"
        ACCOUNT_BALANCE_FROM = "13455 $100.00 $"
        ACCOUNT_BALANCE_TO = "13566 $10.00 $"


    def __init__(self, page):
        super().__init__(page)

    def account_overview_page_open(self):
        self.navigate_to(AppConfiguration.get_common_info()["Url"] + "/overview.htm")

    def check_welcome_message(self):
        common_info = AppConfiguration.get_common_info()
        expect(self.page.get_by_text(self._Selectors.WELCOME_MSG)).to_contain_text(common_info["User"])

    def click_account_number(self):
        self.page.get_by_role("link", name=self._Selectors.ACCOUNT_NUMBER_LINK).click()

    def account_number_verify(self):
        expect(self.page.get_by_role("cell", name=self._Selectors.ACCOUNT_NUMBER_LINK)).to_be_visible()

    def verify_account_balance(self):
        amount_from = self.page.get_by_role("cell", name=self._Selectors.ACCOUNT_BALANCE_FROM).inner_text().strip()
        amount_to = self.page.get_by_role("cell", name=self._Selectors.ACCOUNT_BALANCE_TO).inner_text().strip()

        def extract_balance_amount(text: str) -> float:
            match = re.search(r'\$(\d+(?:\.\d{2})?)', text)
            if match:
                return float(match.group(1))
            raise ValueError(f"No valid dollar amount found in '{text}'")

        amount_only_from = extract_balance_amount(amount_from)
        amount_only_to = extract_balance_amount(amount_to)
        assert (amount_only_to - amount_only_from) == 10.00



