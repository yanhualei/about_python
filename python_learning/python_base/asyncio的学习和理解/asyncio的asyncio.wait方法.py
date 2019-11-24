import asyncio
import time


async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def main():
    tasks = [
        asyncio.ensure_future(do_some_work(1)),
        asyncio.ensure_future(do_some_work(2)),
        asyncio.ensure_future(do_some_work(4))
    ]

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('Task ret: ', task.result())

start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time.time()
print('times: ', end - start)


# asyncio.wait(tasks):此函数返回两个列表：
# dones：已完成的协程任务列表
# pendings：等待的协程任务列表