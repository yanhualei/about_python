
"""
所有类的超类object，有一个默认包含pass的__init__()实现，这个函数会在对象初始化的时候调用，
我们可以选择实现，也可以选择不实现，一般建议是实现的，不实现对象属性就不会被初始化，
虽然我们仍然可以对其进行赋值，但是它已经成了隐式的了，编程时显示远比隐式的更好
"""

class Test_init(object):
    def __init__(self):  # __init__方法可以实现也可以不实现
        self.a = 1
        self.b = 2

    def  func_one(self):
        return self.a,self.b


class Test_init2(object):
    # def __init__(self):  # __init__方法可以实现也可以不实现
    #     self.a = 1
    #     self.b = 2

    def  func_one(self):
        return self.a,self.b  # 隐式定义实例属性


print(vars(Test_init()))  # vars函数获知显示声明的属性，但是隐式的就无法获知了

print(vars(Test_init2()))

test2 = Test_init2()
test2.a = 1  # 隐式定义的实例属性虽然无法被获知，但是也可以被赋值，只是隐式定义罢了
test2.b = 2
print(test2.func_one())




