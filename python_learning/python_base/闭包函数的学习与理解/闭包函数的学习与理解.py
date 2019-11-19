"""什么是闭包函数？"""
#闭包有什么作用？
# 创建闭包是为了实现装饰器

def fun1(a,b):
    def fun2(x):
        print((a+b)*3)  # 内层函数需要参数时，会在内存空间寻找外层函数传递进来的参数
    return fun2  # 指向内层函数


fun1(1,2)(3)
