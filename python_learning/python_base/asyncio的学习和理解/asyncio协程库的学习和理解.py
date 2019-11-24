import asyncio

# async def do_some_work(x): pass   # async定义协程：do_some_work 是一个协程函数
# print(asyncio.iscoroutinefunction(do_some_work))  # 用来验证do_some_work是不是协程函数

async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)  # 让它睡眠几秒，以模拟实际的工作量，await asyncio.sleep(x)其实也是一个协程，她在等待另一个future结束产生结果，或者抛出异常；
    print("well down")

loop = asyncio.get_event_loop()  # 创建循环事件
futu = asyncio.ensure_future(do_some_work(3))  # 将协程任务封装程future对象
loop.run_until_complete(futu)  # 执行loop：通过 run_until_complete 来运行 loop ，等到 future 完成，run_until_complete 也就返回了。
loop.close()  # 可以省略不写，也没有什么问题，但是建议调用 loop.close，以彻底清理 loop 对象防止误用。
# run_until_complete只能运行单个的future
# 如果需要运行多个future，需要用:
# futu = [asyncio.ensure_future(do_some_work(3)),asyncio.ensure_future(do_some_work(3))]
# loop.run_until_complete(asyncio.gather(*futu))

"""
event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。

coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。

task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。

future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别

async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
"""











