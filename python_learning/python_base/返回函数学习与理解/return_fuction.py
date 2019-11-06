# 返回函数学习与理解
#  返回函数：将需要返回的函数封装在外包函数中，那么外部传入的参数和相关变量都存在于返回函数中
from functools import reduce
# def out_function(*args):
#     def return_function():
#         return_sum=0
#         for i in range(*args):
#             return_sum=return_sum+i
#
#         return  return_sum
#     return return_function
#
# r = out_function(10)
# print (r())

# print(out_function(2))  # 直接调用外部函数，返回的则是一个内部函数
# 为什么这样写，当后续程序不需要立即得到结果，而是根据需要再进行运算时，就需要这样闭包操作
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”，据说有相当大的威力-->有待考证

# 继续利用经典案例了解闭包程序
# 在闭包程序中，外部函数传进来的参数相当于全局变量
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 案例一：(此案例为错误案例)
def count():  # 外围函数
    L=[]
    for i in range (1,4):  # i=[1,2,3]
        def f():
            return i*i
        L.append(f)
    return L
#代码解析：i-->1     f1=i*i
            # i-->2    f2=i*i
            # i-->3    f3=i*i
            #此处返回函数引用了i这个可变的变量，当循环第三次时，i-->3,所以得出的结果是[9,9,9]
[f1,f2,f3]=count()
print(f1(),f2(),f3())

# 案例二(完整的闭包函数)#闭包函数缺点：代码太长，可用lambda代替
def r_count():
    lis=[]
    for t in range(1,4):
        def g(x):
            return x * x
        lis.append(g(t))
    return lis

[fun_f1,fun_f2,fun_f3]=r_count()
print(fun_f1(),fun_f2(),fun_f3())
# 代码解析：与案例一相比，本例将传进来的参数t绑定到了x中即，t-->[1,2,3]分别传递到了x--->[1,2,3]
# 这样的话，无论t如何变化，都不影响返回函数最后要返回的值




