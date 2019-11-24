import asyncio
import aiohttp

async def clientsession():
    base_url = 'https://api.github.com/events?a=1'
    headers={}
    conn = aiohttp.TCPConnector(verify_ssl=False, limit=10, limit_per_host=30)  # 防止ssl报错,
    # limit:默认链接数100,limit=0则没有限制
    # limit_per_host:同一端点的最大连接数量。同一端点即(host, port, is_ssl)完全相同.
    # conn.connect(base_url)  # 向目标网站发起链接
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(base_url, headers=headers, timeout=60) as req:  # req返回的是json数据
            text = await req.text()
            print(text)

loop = asyncio.get_event_loop()
loop.run_until_complete(clientsession())