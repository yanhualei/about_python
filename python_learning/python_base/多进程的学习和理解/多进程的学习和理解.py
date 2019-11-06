# 进程：进程就是应用程序的启动实例。比如我们运行一个游戏，打开一个软件，就是开启了一个进程。
# 进程拥有代码和打开的文件资源、数据资源、独立的内存空间。
# 进程由程序，数据集，进程控制块三部分组成
# 进程也是操作系统进行资源分配的最小单位
# 1.能实现多任务
# 2.不能共享全局变量，但是能通过queue队列实现进程间的资源交流
# 3.主线程结束，并不能结束子线程
# 4.多进程切换时消耗资源比较大，效率较低
# 5.进程之间的执行顺序是不确定的
# 6.当如果使用多进程，而不能确定任务数量时，创建进程池解决
import multiprocessing
import time
import os

def sing():
    num = 0
    for i in range(5):
        num += 1
        time.sleep(1)
        print(multiprocessing.current_process(),os.getpid(),":----->sing%s"%num)


def dance():
    num = 0
    for i in range(5):
        num += 1
        time.sleep(1)
        print(multiprocessing.current_process(),os.getpid(),":----->dance%s" % num)

def main():
    p1 = multiprocessing.Process(target=sing)
    p2 =  multiprocessing.Process(target=dance)
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()
