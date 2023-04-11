import asyncio
from aiohttp.client import ClientSession
from nodelesspy.nodeless import Nodeless
from utils import get_api_from_config
from utils import get_api_from_config
import json

"""
Tests for Nodeless SDK Stores
"""

events = [
            "new",
            "pending_confirmation",
            "paid",
            "expired",
            "cancelled",
            "underpaid",
            "overpaid",
            "in_flight"
        ]

type = [
    "store",
    "donation_page",
    "paywall",
    "inbox"
]

status= ["active", "inactive"]


async def main():
    api_key = get_api_from_config("config.yml")
    print("api key from config file: " + str(api_key))

    async with ClientSession() as session:
        node = Nodeless(api_key=api_key, testnet=False, session=session)
        print(f"Nodeless.io api key: {node.api_key}")

        ## Stores
        all_stores = await node.get_stores()
        print(f"Get All Stores: " + json.dumps(all_stores))

        # assume we have a list of stores for testing.
        id = all_stores["data"][0]["id"]
        one_store = await node.get_store(id)
        print(f"Get One Store's Details: " + json.dumps(one_store))

        ## Store Webhooks
        all_hooks = await node.get_store_webhooks(id)
        print(f'\nAll Store Webhooks: ' + json.dumps(all_hooks))

        payload = {
            "type": "inbox",
            "url": "https://nodeless.one",
            "events": ["new"],
            "secret": "WgkicYipQhFARZocnhJX",
            "status": "active",
        }

        # doesn't work with API, error
        #  {"message": "No query results for model [App\\Models\\DonationPage]."}
        create_hook = await node.create_store_webhook(id, payload)
        print(f'\nCreate webhook: ' + json.dumps(create_hook))

        webhookId = all_hooks["data"][0]["id"]
        one_hook = await node.get_store_webhook(id, webhookId)
        print(f'\nWebhook from One Store: ' + json.dumps(one_hook))

        update_payload = {
                "url": "https://utxo.one",
                "events": ["new"],
                "status": "active",
            }
        update_hook = await node.update_store_webhook(id, webhookId, update_payload)
        print(f'\nUpdate Webhook in One Store: ' + json.dumps(update_hook))

        # returns html!? error
        # delete_hook = await node.delete_store_webhook(id, webhookId)
        # print(f'\Delete Store Webhook: ' + json.dumps(delete_hook))

        ## Store Invoices
        payload = {
            "amount": 100.5,
            "currency": "USD",
            "buyerEmail": "keven.sporer@example.net",
            "redirectUrl": "https://nodeless.io",
            "metadata": {
                "key": "value"
            }
        }

        create_invoice = await node.create_store_invoice(id, payload)
        print(f'\nCreate Store Invoice: ' + json.dumps(create_invoice))

        invoiceId = "78920847-2b13-48e3-8272-9faf13eb0da7"
        get_invoice = await node.get_store_invoice(id, invoiceId)
        print(f'\nGet Store Invoice: ' + json.dumps(get_invoice))

        # {"message": "Server Error"}
        invoice_status = await node.get_store_invoice_status(id, invoiceId)
        print(f'\nInvoice Status: ' + json.dumps(invoice_status))



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
