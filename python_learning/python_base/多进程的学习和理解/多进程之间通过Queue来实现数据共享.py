import multiprocessing
"""一个进程向Queue写入数据，另一个进程从Queue读取数据，通过Queue完成了
    多个进程之间的数据交流与共享，从而达到解耦的目的"""

def data(queue):
    lis = [1,2,3,4]
    for i in lis:
        queue.put(i)  # 向queue队列中添加一个数据
        # print(queue.put(i))
    print("==================数据已写入完毕=================")
def get_data(queue):
    get_lis = []
    while True:
        data = queue.get()  # 从queue队列中取一个
        get_lis.append(data)
        if queue.empty():  # 如果queue为空
            break
    print(get_lis)


def main():
    # 创建一个queue队列
    queue = multiprocessing.Queue()
    # 创建一个多进程让test1和test2同时跑起来
    p1 = multiprocessing.Process(target=data,args=(queue,))
    p2 = multiprocessing.Process(target=get_data,args=(queue,))

    p1.start()
    p1.join()  # 等待p1进程运行完毕，在运行进程2
    p2.start()


if __name__ == '__main__':
    main()