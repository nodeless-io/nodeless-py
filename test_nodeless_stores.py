import asyncio
from aiohttp.client import ClientSession
from nodelesspy.nodeless import Nodeless
from utils import get_api_from_config
from utils import get_api_from_config

"""
Tests for Nodeless SDK
"""


async def main():
    api_key = get_api_from_config("config.yml")
    print("api key from config file: " + str(api_key))

    async with ClientSession() as session:
        node = Nodeless(api_key=api_key, testnet=False, session=session)
        print(f"Nodeless.io api key: {node.api_key}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
