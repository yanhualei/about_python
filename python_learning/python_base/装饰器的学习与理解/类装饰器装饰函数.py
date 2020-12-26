class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)  # 此时虽然表面上是类在装饰test,但是真正装饰函数是__call__,所以这个地方要返回func



@CallingCounter
def test():  # test被CallingCounter装饰,所以test就是它的一个实例对象
    print('我被调用了')

test()
test()
print("被调用了%s次"%test.count)



