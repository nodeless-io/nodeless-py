from aiohttp.client import ClientSession
import json

MAIN_NET = "https://nodeless.io/api/"
TEST_NET = "https://testnet.nodeless.io/api/"


class Nodeless:
    def __init__(
        self,
        api_key: str = "",
        session: ClientSession = None,
        testnet: bool = False,
        version: str = "1",
    ):
        self._api_key = api_key
        self._session = session
        self._base_url = f"{TEST_NET}v{version}" if testnet else f"{MAIN_NET}v{version}"

    @property
    def api_key(self):
        return self._api_key

    async def call_api(self, path: str, method: str, body: dict) -> str:
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        print("Call API Url: " + self._base_url + path)
        # print(headers)
        # print(body)

        if method == "GET":
            async with self._session.get(
                url=self._base_url + path, headers=headers, json=body
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
        return "No request Method specified, please define!"

    ## Paywall Requests
    async def create_paywall_request(self, id: str):
        """
        Create a Paywall Request
        """
        url = f"/paywall/{id}/request"
        response = await self.call_api(url, "POST", None)
        return response

    async def get_paywall_request(self, id: str, requestId: str):
        """
        Get a Paywall Request
        """
        url = f"/paywall/{id}/request/{requestId}"
        response = await self.call_api(url, "GET", None)
        return response

    async def get_paywall_request_status(self, id: str, requestId: str):
        """
        Get Paywall Request Status
        """
        url = f"/paywall/{id}/request/{requestId}/status"
        response = await self.call_api(url, "GET", None)
        return response

    ## Paywall Webhooks
    async def get_paywall_webhooks(self, id: str):
        url = f"/paywall/{id}/webhook"
        response = await self.call_api(url, "GET", None)
        return response

    async def create_paywall_webhooks(self, id: str):
        url = f"/paywall/{id}/webhook"
        response = await self.call_api(url, "POST", None)
        return response

    async def get_paywall_webhook(self, id: str, webhookId: str):
        url = f"/paywall/{id}/webhook/{webhookId}"
        response = await self.call_api(url, "GET", None)
        return response

    async def delete_paywall_webhook(self, id: str, webhookId: str):
        url = f"/paywall/{id}/webhook/{webhookId}"
        response = await self.call_api(url, "DELETE", None)
        return response

    async def update_paywell_webhook(self, id: str, webhookId: str):
        url = f"/paywall/{id}/webhook/{webhookId}"
        response = await self.call_api(url, "PUT", None)
        return response

    ## Paywalls
    async def get_paywalls(self):
        """
        Get all the paywalls
        """
        url = "/paywall"
        response = await self.call_api(url, "GET", None)
        return response

    async def create_paywall(self, payload: dict):
        url = "/paywall"
        response = await self.call_api(url, "POST", payload)
        return response

    async def get_paywall(self, id: str):
        """
        Get Paywall by ID
        """
        url = f"/paywall/{id}"
        response = await self.call_api(url, "GET", None)
        return response

    async def update_paywall(self, id: str, payload: dict):
        url = f"/paywall/{id}"
        response = await self.call_api(url, "PUT", payload)
        return response

    async def delete_paywall(self, id: str):
        url = f"/paywall/{id}"
        response = await self.call_api(url, "DELETE", None)
        return response

    ## server info
    async def get_api_status(self):
        """
        Get the server status
        """
        url = "/status"
        response = await self.call_api(url, "GET", None)
        return response

    # Store Invoices
    async def create_store_invoice(self, id: str, payload: dict):
        """
        Create Store Invoice
        """
        url = f"/store/{id}/invoice"
        response = await self.call_api(url, "POST", payload)
        return response

    async def get_store_invoice(self, id: str, invoiceId: str):
        """
        Get Store Invoice
        """
        url = f"/store/{id}/invoice/{invoiceId}"
        response = await self.call_api(url, "POST", None)
        return response

    async def get_store_invoice_status(self, id: str, invoiceId: str):
        """
        Get Store Invoice Status
        """
        url = f"/store/{id}/invoice/{invoiceId}/status"
        response = await self.call_api(url, "GET", None)
        return response

    # Store Webhooks
    async def get_store_webhooks(self):
        """
        Displays a list of webhooks belonging to the store.
        """
        url = f"/store/{id}/webhook"
        response = await self.call_api(url, "GET", None)
        return response

    async def create_store_webhook(self, id: str, payload: dict):
        url = f"/store/{id}/webhook"
        response = await self.call_api(url, "POST", payload)
        return response

    async def get_store_webhook(self, id: str, webhookId: str):
        url = f"/store/{id}/webhook/{webhookId}"
        response = await self.call_api(url, "GET", None)
        return response

    async def delete_store_webhook(self, id: str, webhookId: str):
        url = f"/store/{id}/webhook/{webhookId}"
        response = await self.call_api(url, "DELETE", None)
        return response

    async def update_store_webhook(self, id: str, webhookId: str, payload: dict):
        url = f"/store/{id}/webhook/{webhookId}"
        response = await self.call_api(url, "PUT", payload)
        return response

    ## Stores
    async def get_stores(self):
        """
        Displays a list of stores belonging to the authenticated user.
        """
        url = "/store"
        response = await self.call_api(url, "GET", None)
        return response

    async def get_store(self, id: str):
        """
        Displays a store's details.
        """
        url = f"/store/{id}"
        response = await self.call_api(url, "GET", None)
        return response

    ## transactions
    async def get_all_transactions(self):
        """
        Get all transactions
        """
        url = "/transaction"
        response = await self.call_api(url, "GET", None)
        return response

    async def get_transaction(self, id: str):
        """
        Get a single transaction
        """
        url = f"/transaction/{id}"
        response = await self.call_api(url, "GET", None)
        return response
