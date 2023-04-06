import asyncio
from aiohttp.client import ClientSession
from .. nodelesspy.nodeless import Nodeless

"""
Tests for Nodeless SDK
"""

async def main():
    node = Nodeless(config_file="config.yml")

    async with ClientSession() as session:
        print(f"apikey: {node.apikey}")
        print("test paywall")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
