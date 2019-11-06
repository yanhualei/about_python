import random
import timeit


def test():
    my_list = random.sample(range(2000000), 1000000)  # 从0-1999999中随机取出1000000个数据，并且返回
    sorted(my_list)


if __name__ == '__main__':

    print(timeit.timeit("test()","from __main__ import test",number=1))

    # 第一个参数：要执行计时的语句模块(函数)
    # 第二个参数setup用于构建代码环境，可以用来导入需要的模块
    # 最后的number指定了运行的次数。