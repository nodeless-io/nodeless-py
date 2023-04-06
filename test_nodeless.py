import asyncio
from aiohttp.client import ClientSession
from nodelesspy.nodeless import Nodeless

from yaml import safe_load
import json

"""
Tests for Nodeless SDK
"""


def get_api_from_config(config_file):
    try:
        if config_file:
            with open(config_file, "rb") as f:
                cfile = safe_load(f)
                api_key = cfile["apikey"]
                return api_key
            f.close()
    except Exception as e:
        return e


async def main():
    api_key = get_api_from_config("config.yml")
    print("api key from config file: " + str(api_key))

    async with ClientSession() as session:
        node = Nodeless(api_key=api_key, testnet=False, session=session)

        print(f"Nodeless.io api key: {node.api_key}")
        status = await node.get_api_status()

        print("** Server Info **")
        print("Get API Status: " + json.dumps(status))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
