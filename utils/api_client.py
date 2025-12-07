import logging
import requests
from requests.auth import HTTPBasicAuth
from utils.read_config import AppConfiguration

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url, self.username, self.password = self._get_config()
        self.auth = HTTPBasicAuth(self.username, self.password)
        self.session.auth = self.auth
        logger.info(f"APIClient initialized with base_url: {self.base_url}")

    def _get_config(self):
        try:
            common_info = AppConfiguration.get_common_info()
            base_url = common_info.get("BaseApiUrl", "https://parabank.parasoft.com/parabank/services/bank")
            username = common_info.get("UserName", "john")
            password = common_info.get("Password", "demo")
            return base_url, username, password
        except Exception:
            logger.warning("Config load failed; using defaults")
            return "https://parabank.parasoft.com/parabank/services/bank", "john", "demo"

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, **kwargs)
        logger.info(f"GET {url}: {response.status_code}")
        return response

    def post(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, **kwargs)
        logger.info(f"POST {url}: {response.status_code}")
        return response

    def put(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, **kwargs)
        logger.info(f"PUT {url}: {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, **kwargs)
        logger.info(f"DELETE {url}: {response.status_code}")
        return response