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

        ## Stores
        all_stores = await node.get_stores()
        print(f'Get All Stores: ' + json.dumps(all_stores))

        # assume we have a list of stores for testing.
        id = all_stores['data'][0]['id']
        one_store = await node.get_store(id)
        print(f'Get One Store\'s Details: ' + json.dumps(one_store))


        ## Store Webhooks
        payload = {
            "type": "donation_page",
            "url": "https:\/\/www.kuhn.com\/nulla-velit-non-repudiandae-voluptas-deleniti-neque-dolores-dolores",
            "events": [
                "expired"
            ],
            "secret": "voluptates",
            "status": "active"
        }
        

        ## Store Invoices
        # store_invoice = await node.create_store_invoice()
        # print(f'Create Store Invoice: ' + json.dumps(store_invoice))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
