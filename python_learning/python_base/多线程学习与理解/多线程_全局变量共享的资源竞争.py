import threading
import time

num = 0

def test1(number):
    global num
    #mutex.acquire()  # 这样加锁的话，结果不会有错，但程序跟单线程没什么区别
    for i in range(number):
        mutex.acquire()  # 这样加锁的话，结果先执行完的结果比1000000大，后执行的结果仍然是2000000，原因就是全局变量的共享而导致的
        num += 1
        mutex.release()
    #mutex.release()
    print("-----test1_total:%s------"%num)
def test2(number):
    global num
    #mutex.acquire()
    for i in range(number):
        mutex.acquire()
        num += 1
        mutex.release()
    #mutex.release()
    print("-----test2_total:%s------" % num)

# 创建一个互斥锁，默认没有上锁
mutex =  threading.Lock()
def main():
    t1 = threading.Thread(target=test1, args=(10000000,))
    t2 = threading.Thread(target=test2, args=(10000000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("-----the mainthread:%s------"%num)

if __name__ == '__main__':
    main()