import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

from tools import config, env


def _build_session() -> requests.Session:
    """Create a requests Session with automatic retries for transient errors."""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session


_session = _build_session()


class StarlingClient:
    """Thin wrapper around the Starling Bank API v2."""

    def __init__(self,access_token):
        self.access_token = access_token
        self.base_url = config("BASE_URL")

    @property
    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def __call__(
        self,
        endpoint: str,
        body: dict | None = None,
        params: dict | None = None,
        method: str = "GET",
    ):
        """Make a call to the Starling API."""

        url = f"{self.base_url}{endpoint}"
        time.sleep(config("API_COOLDOWN"))
        response = _session.request(
            method, url, headers=self._headers, json=body, params=params
        )

        match response.status_code:
            case 200:
                return response.json()

            case 202:
                data = response.json()
                print("Request accepted, polling data: %s", data)
                return None

            case 204:
                print("No content returned from %s", endpoint)
                return None

            case 400:
                print("Bad request to %s: %s", endpoint, response.text)
                raise ValueError(f"Bad request: {response.text}")

            case 401:
                print("Invalid authentication credentials")
                raise PermissionError("Unauthorized: check your access token")

            case 403:
                print("Forbidden: token may be expired or lack scope for %s", endpoint)
                raise PermissionError(f"Forbidden: {response.text}")

            case 404:
                print("Resource not found: %s", endpoint)
                raise FileNotFoundError(f"Not found: {url}")

            case _ if response.status_code >= 500:
                print(
                    "Starling server error %s: %s", response.status_code, response.text
                )
                raise ConnectionError(
                    f"Server error {response.status_code}: {response.text}"
                )

            case _:
                print("Unexpected status %s: %s", response.status_code, response.text)
                raise Exception(
                    f"Unexpected error {response.status_code}: {response.text}"
                )


if __name__ == "__main__":
    api = StarlingClient()
    print(api("/api/v2/accounts"))
