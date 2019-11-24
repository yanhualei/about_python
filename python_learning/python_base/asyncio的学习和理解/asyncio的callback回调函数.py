import asyncio


async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)
    return  "well down"

def done_callback(futu):
    print('Done')

loop = asyncio.get_event_loop()  # 创建循环事件
futu = asyncio.ensure_future(do_some_work(3))  # 把携程对象封装程future
futu.add_done_callback(done_callback)  # 向futu中添加回调函数：
loop.run_until_complete(futu)  # 执行协程任务
print(futu.result())  # futu.result():获取协程任务返回的结果
# 什么是回调函数？
# 在本例中：也就是do_some_work协程任务结束之后，会去调用done_callback函数，得到done_callback的返回结果