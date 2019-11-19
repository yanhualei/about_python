import datetime
# __repr__ 目的是为了表示清楚，是为开发者准备的。返回对象来源的类以及继承关系，以字符串形式返回
#
# __str__ 目的是可读性好，是为使用者准备的。直接返回对象，以字符串形式返回
#
# 我的理解是 __repr__ 应该尽可能的表示出一个对象来源的类以及继承关系，方便程序员们了解这个对象。而 __str__ 就简单的表示对象，而不要让不懂编程的以为输出的是 bug。



class  Test_repr(object):
    def __init__(self):
        self.time = datetime.datetime.now()

    def __repr__(self):  # 用于格式化输出，执行print(obj)时，会自动调用
        return "The time is:{}".format(self.time)



test_str = Test_repr()
print(repr(test_str))
print(str(test_str))

# 结果为什么打印的是一样的，原因是print会自动调用__str__这个魔法方法
# 验证这两个魔法方法不一样之处，可用python console
# import datetime
# date = datetime.datetime.now()
# str(date)
# repr(date)