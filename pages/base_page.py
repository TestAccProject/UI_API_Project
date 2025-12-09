import logging
from playwright.sync_api import Page, expect
from utils.read_config import AppConfiguration


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_text(locator):
    text = locator.inner_text()
    logger.debug(f"Extracted text from {locator}: {text}")
    return text


class BasePage:
    class _Selectors:
        pass

    def __init__(self, page: Page):
        self.page = page
        self.timeout = self._get_timeout()  
        logger.info(f"Initialized BasePage with timeout: {self.timeout}ms")

    def _get_timeout(self):
        try:
            configuration = AppConfiguration.get_app_configuration()
            return float(configuration.get("DefaultTimeout", 30000))
        except (KeyError, ValueError, Exception):
            logger.warning("Config load failed; using default timeout 30000ms")
            return 30000

    def navigate_to(self, url: str):
        self.page.goto(url)
        logger.info(f"Navigated to: {url}")

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout or self.timeout
        expect(locator).to_be_visible(timeout=timeout // 1000)
        locator.click()
        logger.info(f"Clicked: {locator}")

    def wait_and_fill(self, locator, text: str, timeout=None):
        timeout = timeout or self.timeout
        expect(locator).to_be_visible(timeout=timeout // 1000)
        locator.fill(text)
        logger.info(f"Filled {locator} with: {text}")
