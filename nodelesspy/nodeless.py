import requests
from yaml import safe_load
from aiohttp.client import ClientSession
import json
import os

MAIN_NET = "https://nodeless.io/api/"
TEST_NET = "https://testnet.nodeless.io/api/"


class Nodeless:
    def __init__(
        self,
        config_file: str = "",
        apikey: str = None,
        session: ClientSession = None,
        testnet: bool = False,
    ):
        self._config_file = config_file
        self._api_key = apikey
        self._session = session
        self._base_url = TEST_NET if testnet else MAIN_NET

        try:
            if config_file:
                with open(config_file, "rb") as f:
                    cfile = safe_load(f)
                f.close()
        except Exception as e:
            return e

    @property
    def config_file(self):
        return self._config_file

    @property
    def api_key(self):
        return self._apikey

    async def call_api(self, path: str, method: str, body: str) -> str:
        headers = {
            "Authorization": "Bearer {self._apikey}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        if method == "GET":
            async with self._session.get(
                url=self._base_url + path, headers=headers, data=body
            ) as response:
                return response.json()
        elif method == "POST":
            async with self._session.post(
                url=self._base_url + path, headers=headers, data=body
            ) as response:
                return response.json()
        elif method == "PUT":
            async with self._session.put(
                url=self._base_url + path, headers=headers, data=body
            ) as response:
                return response.json()
        elif method == "DELETE":
            async with self._session.delete(
                url=self._base_url + path, headers=headers, data=body
            ) as response:
                return response.json()

    ## Paywalls
    async def get_paywalls(self):
      url=f'/api/v1/paywall'
      response = await self.call_api(url, 'GET', {})
      return response

    async def create_paywall(self):
      url=f'/api/v1/paywall'
      response = await self.call_api(url, 'GET', {})
      return response
    
    async def get_paywall(self):
      url=f'/api/v1/paywall'
      response = await self.call_api(url, 'GET', {})
      return response

    async def update_paywall(self):
      url=f'/api/v1/paywall'
      response = await self.call_api(url, 'GET', {})
      return response
    
    async def delete_paywall(self):
      url=f'/api/v1/paywall'
      response = await self.call_api(url, 'GET', {})
      return response

    ## Paywall requests
    async def create_paywall_request(self, id: str):
        url = f"/v1/paywall/{id}/request"
        response = await self.call_api(url, "POST", {})
        return response
    
    ## server info
    async def get_api_status(self):
        url = f''
        response = await self.call_api(url, "GET", {})
        return response


