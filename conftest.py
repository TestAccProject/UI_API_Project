import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
import pytest
from endpoints.login_endpoint import LoginEndpoint
from utils.read_config import AppConfiguration
import logging

pytest_plugins = ["pytest_playwright"]
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type, pytestconfig):
    configuration = AppConfiguration.get_app_configuration()
    headless_value = configuration["Headless"]
    if isinstance(headless_value, bool):
        headless = headless_value
    else:
        headless_str = str(headless_value).strip().lower()
        headless = headless_str == "true"
    slow_mo = float(configuration["SlowMo"])
    return {
        "headless": headless,
        "slow_mo": slow_mo,
        "args": ["--start-maximized"]
    }


@pytest.fixture(scope="session")
def browser_context_args(pytestconfig):
    configuration = AppConfiguration.get_app_configuration()
    common_info = AppConfiguration.get_common_info()

    return {
        "base_url": common_info["Url"],
        "no_viewport": True,
        "viewport": None,
    }


@pytest.fixture(scope="session")
def context(browser, browser_context_args, default_navigation_timeout, default_timeout):
    context = browser.new_context(**browser_context_args)
    context.set_default_timeout(default_timeout)
    context.set_default_navigation_timeout(default_navigation_timeout)

    yield context

    context.close()


@pytest.fixture(scope="session")
def default_navigation_timeout(pytestconfig):
    configuration = AppConfiguration.get_app_configuration()
    return float(configuration["DefaultNavigationTimeout"])


@pytest.fixture(scope="session")
def default_timeout(pytestconfig):
    configuration = AppConfiguration.get_app_configuration()
    return float(configuration["DefaultTimeout"])


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    yield page

    page.close()


@pytest.fixture(scope="function")
def setup(request, page):
    if request.cls is not None:
        request.cls.page = page

    yield page



@pytest.fixture(scope="session")
def customer_id():
    login_endpoint = LoginEndpoint()
    customer_id = login_endpoint.login()
    logger.info(f"Logged in; customerId: {customer_id}")

    yield customer_id