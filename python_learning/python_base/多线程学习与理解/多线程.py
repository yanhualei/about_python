# 线程：
# 1.是CUP调度的最小单位
# 2.优点：占用资源相对较小，效率较高
# 3.全局变量是共享的
# 4.主线程结束，子线程相应的也会结束
# 5.线程依赖于进程
# 6.在 Python 中，无论是单核还是多核，一个进程同时只能由一个线程在执行。其他语言，CPU 是多核时是支持多个线程同时执行
import threading
import time
"""每个程序运行至少会有一个进程和一个线程"""
print("演示多线程运行过程，从而理解多线程")
def sing():
    for i in range(5):
        print(threading.current_thread().name, ":-----正在唱歌-----",i)
        time.sleep(1)


def dance():
    for i in range(5):
        print(threading.current_thread().name, ":-----正在跳舞-----",i)
        time.sleep(1)


def main():
    print(threading.current_thread().name)
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    """1、当主线程运行到t1.start()，主线程会产生一个子线程，称为子线程的诞生处，是第一个子线程生命开始的地方
       2、主线程继续运行，同时第一个子线程会跑到sing()运行"""

    t1.start()

    """1、当主线程运行到t2.start()，主线程又会产生一个子线程，是第二个子线程生命开始的地方
       2、主线程继续运行，同时第一个子线程会跑到dance()运行"""
    t2.start()
    t1.join() #  线程1完成所有任务后，加入到主线程
    t2.join()  # 线程2完成所有任务后加入到主线程
    # 所以join的作用就是让子线程和主线程同步，即主线程完成任务之后，进入阻塞状态，
    #一直等待其他子线程执行完毕之后，主线程再终止
    print("主线程结束")
if __name__ == '__main__':
    main()
    """如果没有join，t2.start()运行完之后，主线程会返回到main()的调用处，但主线程不会结束，而是会等待线程1和线程2结束之后，
    主线程才会结束
    """

# 多线程中不t.join()：
# 主线程不会在这一行停留，会直接往下运行，直到没有代码运行，主线程不会影响子线程的运行
# 子线程同时也在运行，子线程的继续运行也不会影响主线程的结束

# 多线程中添加t.join():
# 主线程遇到join会在join处等待子线程的执行结果，子线程任务执行完毕，主线程才会回收子线程，
# 然后主线程继续向下执行