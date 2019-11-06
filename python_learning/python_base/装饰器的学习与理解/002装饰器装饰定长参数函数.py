def test1(func):
    def test2(a):
        print("--权限验证1--")
        print("--权限验证2--")
        return func(a)  # func==>now==>print('2016-3-25')
    return test2

@test1 # = now = test1(now)
def now(a):
    print(a)
now(2)

"""装饰器对带固定个数参数函数的装饰"""
