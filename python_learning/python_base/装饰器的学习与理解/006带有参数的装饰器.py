""""""
"""带有参数的装饰器：
为什么要创建带参数的装饰器？
    ===>因为装饰器添加的功能需要接收外部传参数
怎么创建带参数的装饰器？
    ===>在普通的装饰器外部再添加一层函数，用于传递参数
带参数的装饰器有什么用处？
    ===>为添加的功能传递参数


"""
def num_func(num):
    def set_func(func):
        def call_func(*args,**kwargs):
            if num ==1:
                print("这是权限验证1")
            if num == 2:
                print("这是权限验证2")
            return func(*args,**kwargs)
        return call_func
    return set_func
@num_func(2) # test = set_func(test)
def test1():
    print("这是原函数...")

@num_func(1) # test = set_func(test)
def test2():
    print("这是原函数...")
test1()
test2()

"""这段带参数的装饰器在没有改变原函数的情况下，
把权限验证加载到了原函数上，也就是说，如果装饰器
添加的功能需要参数，那么就在普通装饰器上再加一层函数，
用来传递参数就行了"""

