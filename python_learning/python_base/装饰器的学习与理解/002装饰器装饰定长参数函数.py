def test1(func):
    def test2(a):
        print("--权限验证1--")
        print("--权限验证2--")
        return func(a)
    return test2

@test1
def now(a):
    print(a)
now(2)

"""装饰器对带固定个数参数函数的装饰"""
