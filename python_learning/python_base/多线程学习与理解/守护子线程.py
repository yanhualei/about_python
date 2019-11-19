
import threading
import time
"""每个程序运行至少会有一个进程和一个线程"""
print("演示多线程运行过程，从而理解多线程")
def sing():
    for i in range(5):
        print(threading.current_thread().name, ":-----正在唱歌-----",i)
        time.sleep(1)


def eat():
    for i in range(5):
        print(threading.current_thread().name, ":-----正在吃饭-----",i)
        time.sleep(0.5)


def main():
    print(threading.current_thread().name)
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=eat)
    # 设置t2为守护子线程
    t1.setDaemon(True)
    t1.start()
    # t2.setDaemon(True)
    t2.start()

if __name__ == '__main__':
    main()
    print("主进程结束")


# 什么是守护进程/线程？
#  可以理解为不重要的线程就可以设置为守护进程/线程
#  比如程序中的垃圾回收