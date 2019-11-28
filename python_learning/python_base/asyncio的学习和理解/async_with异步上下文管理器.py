import aiohttp
import asyncio

async def fetch(client):
    async with client.get('https://github.com/') as response:
        # print(type(response))
        # return await response.text()
        return await response.text() # await 后面跟的是一个耗时操作，而不是一个具体的对象

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        response = await fetch(client)
        print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
