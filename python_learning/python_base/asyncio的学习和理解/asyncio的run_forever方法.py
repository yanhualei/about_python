import asyncio
import functools


async def do_some_work(x):
    print('Waiting ' + str(x))
    await asyncio.sleep(x)
    print('Done')

def done_callback(loop, futu):
    loop.stop()  # loop.stop()尽量写在回调函数中

loop = asyncio.get_event_loop()

futus = asyncio.gather(do_some_work(1), do_some_work(3))
futus.add_done_callback(functools.partial(done_callback, loop))

loop.run_forever()
# loop.close()   # 这样关闭不了loop的无限循环，因为run_forever会阻塞程序，除非协程任务主动结束，否则loop.close()不会运行