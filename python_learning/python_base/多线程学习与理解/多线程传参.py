import threading
import time

num = 100
num2 = 1
print("演示多线程全局变量共享和参数传递")
def test1(number):
    # 修改全局变量的指向的时候，需要在函数内部用global声明一下
    # 如果num是个可变变量，例如字典或者列表，则不用global声明
    global num,num2
    num += num2
    print("-----thread1:%s------"%num)
def test2(number):
    print("-----thread2:%s------" % num)


def main():
    # target指定这个线程去哪个函数执行代码
    # args指定执行函数代码的时候，传递什么参数过去
    # args保存的参数是个元组
    t1 = threading.Thread(target=test1, args=(num2,))
    t2 = threading.Thread(target=test2, args=(num2,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("-----the mainthread:%s------"%num)

if __name__ == '__main__':
    main()