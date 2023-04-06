from aiohttp.client import ClientSession
import json

MAIN_NET = "https://nodeless.io/api/"
TEST_NET = "https://testnet.nodeless.io/api/"


class Nodeless:
    def __init__(
        self,
        api_key: str = None,
        session: ClientSession = None,
        testnet: bool = False,
    ):
        self._api_key = api_key
        self._session = session
        self._base_url = TEST_NET if testnet else MAIN_NET

    @property
    def api_key(self):
        return self._api_key

    async def call_api(self, path: str, method: str, body: str) -> str:
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        print("Call API Url: " + self._base_url + path)
        print(headers)
        print(body)
        if method == "GET":
            async with self._session.get(
                url=self._base_url + path, headers=headers, data=body
            ) as response:
                result = await response.json()
                return result
        elif method == "POST":
            async with self._session.post(
                url=self._base_url + path, headers=headers, json=body
            ) as response:
                result = await response.json()
                return result
        elif method == "PUT":
            async with self._session.put(
                url=self._base_url + path, headers=headers, json=body
            ) as response:
                result = await response.json()
                return result
        elif method == "DELETE":
            async with self._session.delete(
                url=self._base_url + path, headers=headers, json=body
            ) as response:
                result = await response.json()
                return result

    ## Paywalls
    async def get_paywalls(self):
        """
        Get all the paywalls
        """
        url = f"v1/paywall"
        response = await self.call_api(url, "GET", {})
        return response

    async def create_paywall(self, payload: json):
        url = f"v1/paywall"
        response = await self.call_api(url, "POST", payload)
        return response

    async def get_paywall(self, id: str):
        """
        Get Paywall by ID
        """
        url = f"v1/paywall/{id}"
        response = await self.call_api(url, "GET", {})
        return response

    async def update_paywall(self, id: str, payload: json):
        url = f"v1/paywall/{id}"
        response = await self.call_api(url, "PUT", payload)
        return response

    async def delete_paywall(self, id: str):
        url = f"v1/paywall/{id}"
        response = await self.call_api(url, "DELETE", {})
        return response

    ## server info
    async def get_api_status(self):
        """
        Get the server status
        """
        url = f"v1/status"
        response = await self.call_api(url, "GET", {})
        return response

    ## transactions
    async def get_all_transactions(self):
        """
        Get all transactions
        """
        url = f"v1/transaction"
        response = await self.call_api(url, "GET", {})
        return response


    async def get_transaction(self, id: str):
        """
        Get a single transaction
        """
        url = f"v1/transaction/{id}"
        response = await self.call_api(url, "GET", {})
        return response
