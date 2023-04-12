import asyncio
from aiohttp.client import ClientSession
from nodelessio.nodeless import Nodeless
from utils import get_api_from_config
import json


"""
Tests for Nodeless SDK Server
"""


async def main():
    api_key = get_api_from_config("config.yml")
    print("api key from config file: " + str(api_key))

    async with ClientSession() as session:
        node = Nodeless(api_key=api_key, testnet=False, session=session)
        print(f"Nodeless.io api key: {node.api_key}")

        print("\n** Server Info **")
        status = await node.get_api_status()
        print("Get API Status: " + json.dumps(status))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
