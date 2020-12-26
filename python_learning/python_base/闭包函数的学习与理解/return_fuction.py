# 返回函数学习与理解
#  返回函数：将需要返回的函数封装在外包函数中，那么外部传入的参数和相关变量都存在于返回函数中
from functools import reduce
def out_function(*args):
    def inturn_function():
        return_sum=0
        for i in range(*args):
            return_sum=return_sum+i
        return  return_sum
    return inturn_function

r = out_function(10)
print (r())

# print(out_function(2))  # 直接调用外部函数，返回的则是一个内部函数
# 为什么这样写，当后续程序不需要立即得到结果，而是根据需要再进行运算时，就需要这样闭包操作
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”

# 在闭包程序中，外部函数传进来的参数相当于全局变量
#返回闭包时牢记一点：返回函数不要引用循环变量，或者后续会发生变化的变量
# 案例一：(此案例为错误案例)
def count():  # 外围函数
    L=[]
    for i in range (1,4):  # i=[1,2,3]
        def f():
            return i*i
        L.append(f)  #闭包函数此时外部函数只是指向了f函数并没有将参数带进去运行,只是到了最后一次去寻找外部函数的参数
    return L
#代码解析：为什么结果出现[999]：因为for循环的时候L列表保存的是[def f():return i*i,def f():return i*i,def f():return i*i],
# 闭包函数，外层函数全部运行结束，才会进入内部函数执行，也就是说内部函数是不会执行的，外部函数执行完也就是i=3的时候，所以结果是[999]
print([fun() for fun in count()])  # count()返回的是一个列表

# 案例二(完整的闭包函数)#闭包函数缺点：代码太长，可用lambda代替
def r_count():
    lis=[]
    for t in range(1,4):
        def g(x):
            return x * x
        lis.append(g(t))
    return lis

result=r_count()
print(result)
# 代码解析：为什么结果是[1,4,9]呢？因为外部函数每次运行的时候要将参数t传到内部函数，所以是[g(1),g(2),g(3)]



