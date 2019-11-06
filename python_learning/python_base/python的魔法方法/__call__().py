# 对象通过提供__call__()方法可以模拟函数的行为，如果一个对象提供了该方法，就可以像函数一样使用它

class Test_call:
    def __init__(self):
        pass

    def __call__(self, x,*args, **kwargs):
        return "the value is %s"%x

test = Test_call()
print(test(100))  # 实例对象可以当做函数一样被使用







