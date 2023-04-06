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

        print("\n** Server Info **")
        status = await node.get_api_status()
        print("Get API Status: " + json.dumps(status))

        print("\n** Get paywalls **")

        payload = {
            "name": "yzfterrucckaksq",
            "type": "redirect",
            "price": 1629
        }
        create_paywall = await node.create_paywall(payload)
        print("Create paywall: " + json.dumps(create_paywall))

        paywalls = await node.get_paywalls()
        paywall_data = json.dumps(paywalls)
        print("Get paywalls: " + paywall_data)

        # get single paywall id, the first one in list
        paywall_id = paywalls['data'][0]['id']
        print(paywall_id)

        get_paywall = await node.get_paywall(paywall_id)
        print("Get Paywall by ID: " + json.dumps(get_paywall))

        update_payload = {
            "name": "yzfterrucckaksq",
            "type": "redirect",
            "price": 2700
        }

        # server error on update, unclear why
        update_paywall = await node.update_paywall(paywall_id, update_payload)
        print("Update Paywall: " + json.dumps(update_paywall))

        delete_paywall = await node.delete_paywall(paywall_id)
        print("Delete paywall: " + json.dumps(delete_paywall))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())



        # print("\n** Paywall Requests **")
        # id = ""
        # request = await node.create_paywall_request(id)
        # print("Create paywall request: " + json.dumps(request))
