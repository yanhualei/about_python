import aiohttp, asyncio


async def main():  # aiohttp必须放在异步函数中使用
    tasks = []
    [tasks.append(fetch('https://api.github.com/events?a={}'.format(i))) for i in range(10)]  # 十次请求
    await asyncio.wait(tasks)


async def fetch(url):
    async with aiohttp.request('GET', url) as resp:  # resp是返回的json文本
        json = await resp.json()
        print(json)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())