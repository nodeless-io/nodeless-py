import asyncio
from aiohttp.client import ClientSession
from nodelessio.nodeless import Nodeless

from utils import get_api_from_config
import json

"""
Tests for Nodeless SDK Paywalls
"""


async def main():
    api_key = get_api_from_config("config.yml")
    print("api key from config file: " + str(api_key))

    async with ClientSession() as session:
        node = Nodeless(api_key=api_key, testnet=False, session=session)
        print(f"Nodeless.io api key: {node.api_key}")

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
        paywall_id = paywalls["data"][0]["id"]
        print(paywall_id)

        get_paywall = await node.get_paywall(paywall_id)
        print("Get Paywall by ID: " + json.dumps(get_paywall))

        update_payload = {
            "name": "yzfterrucckaksq",
            "type": "redirect",
            "price": 2700
        }

        update_paywall = await node.update_paywall(paywall_id, update_payload)
        print("Update Paywall: " + json.dumps(update_paywall))

        # Paywall Requests
        print("\n** Paywall Requests **")
        create_paywall_req = await node.create_paywall_request(paywall_id)
        print("\nCreate Paywall Request: " + json.dumps(create_paywall_req))

        requestId = create_paywall_req["data"]['id']
        get_req = await node.get_paywall_request(paywall_id, requestId)
        print("\n Get paywall request: " + json.dumps(get_req))

        req_status = await node.get_paywall_request_status(paywall_id, requestId)
        print("\n Request Status: " + json.dumps(req_status))

        # Paywall Webhooks
        print("\n** Get paywall webhooks **")
        paywall_hooks = await node.get_paywall_webhooks(paywall_id)
        print(f"\n Get Paywall webhooks: " + json.dumps(paywall_hooks))

        hooks_payload = {
            "type": "paywall",
            "url": "https://harvey.biz/",
            "events": [
                "cancelled"
            ],
            "secret": "est",
            "status": "inactive"
        }

        create_hook = await node.create_paywall_webhook(paywall_id, hooks_payload)
        print(f"\nCreate Paywall webhook: " + json.dumps(create_hook))

        webhookId = create_hook["data"]["id"]
        paywall_hook = await node.get_paywall_webhook(paywall_id, webhookId)
        print(f'Get Paywall Webhook: ' + json.dumps(paywall_hook))

        update_hooks_payload = {
                "type": "paywall",
                "url": "https://funny.biz/",
                "events": [
                    "cancelled"
                ],
                "secret": "est",
                "status": "inactive"
            }

        update_hook = await node.update_paywall_webhook(paywall_id, webhookId, update_hooks_payload)
        print(f'Update Paywall Webhook: ' + json.dumps(update_hook))

        webhookId = update_hook["data"]["id"]

        delete_hook = await node.delete_paywall_webhook(paywall_id, webhookId)
        print(f'Delete Paywall Webhook')

        delete_paywall = await node.delete_paywall(paywall_id)
        print("Delete paywall: " + json.dumps(delete_paywall))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
