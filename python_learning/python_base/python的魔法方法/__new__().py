# 1__new__():
"""
在object类中存在一个静态的__new__(cls, *args, **kwargs)方法，
该方法需要传递一个参数cls，cls表示需要实例化的类，此参数在实例化时由Python解释器自动提供，
__new__方法必须有返回值，且返回的是被实例化的实例，
只有在该实例返回后才会调用__init__来进行初始化，初始化所用的实例就是__new__返回的结果，
也就可以认为是self
"""

class Test_new(object):
    def __init__(self):
        print("__init__被调用")

    def __new__(cls, *args, **kwargs):
        print("__new__被调用")
        return object.__new__(cls)
Test_new()
