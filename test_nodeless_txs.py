import asyncio
from aiohttp.client import ClientSession
from nodelesspy.nodeless import Nodeless
from utils import get_api_from_config
from utils import get_api_from_config
import json

"""
Tests for Nodeless SDK
"""


async def main():
    api_key = get_api_from_config("config.yml")
    print("api key from config file: " + str(api_key))

    async with ClientSession() as session:
        node = Nodeless(api_key=api_key, testnet=False, session=session)
        print(f"Nodeless.io api key: {node.api_key}")

        all_tx = await node.get_all_transactions()
        print(f"All Txs: " + json.dumps(all_tx))

        ## assume there is at least 1 tx already
        first_id = all_tx["data"][0]["id"]

        one_tx = await node.get_transaction(first_id)
        print(f"One Tx: " + json.dumps(one_tx))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
