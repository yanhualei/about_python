import asyncio


async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)

def done_callback(futu):
    print('Done')

loop = asyncio.get_event_loop()
futus = [asyncio.ensure_future(do_some_work(1)),
        asyncio.ensure_future(do_some_work(3))]  # future对象列表
futus[0].add_done_callback(done_callback)  # 为第一个future添加回调函数

loop.run_until_complete(asyncio.gather(*futus))  # 执行多个协程任务