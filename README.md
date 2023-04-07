# nodeless-py

An asyncio/aiohttp python library of methods for accessing nodeless API. 

## Getting Started

version at least python3.8

```
git clone https://github.com/nodeless-io/nodeless-py
cd pylnbits
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Usage

Replace YOUR_AUTH_KEY with your api key.

```
import asyncio
from aiohttp.client import ClientSession
from nodelesspy.nodeless import Nodeless
import json

async def main():

    async with ClientSession() as session:
        node = Nodeless(api_key=YOUR_AUTH_KEY, testnet=False, session=session)
        print(f"Nodeless.io api key: {node.api_key}")

        all_tx = await node.get_all_transactions()
        print(f"All Txs: " + json.dumps(all_tx))

        ## assume there is at least 1 tx already
        first_id = all_tx["data"][0]["id"]

        one_tx = await node.get_transaction(first_id)
        print(f"One Tx: " + json.dumps(one_tx))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Build

Build for distribution:

```
pip install setuptools wheel
python setup.py sdist bdist_wheel
```
