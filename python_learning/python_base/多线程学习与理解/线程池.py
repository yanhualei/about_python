from multiprocessing.dummy import Pool as thread_pool
import datetime
import time


def fun(tem):
    print(tem)
    time.sleep(1)

if __name__ == '__main__':
    begin = datetime.datetime.now()
    print(begin )
    async_pool=thread_pool(processes=5)
    results = []

    for i in range(10):
        result = async_pool.apply_async(fun, (i, ))
        print(result)
        results.append(result)

    for i in results:
        i.wait()
    end = datetime.datetime.now()
    used_time = (end - begin)
    print(used_time)

