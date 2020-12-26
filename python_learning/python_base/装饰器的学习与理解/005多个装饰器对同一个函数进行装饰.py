def test(func):  #3. 此时fucn就是传进来的test2函数
    print("--开始装饰器test--%s"%func.__name__)
    def test4():
        print("--这是总装饰器a的功能--%s"%func.__name__)
        return func()  #5. 指向test2函数并且运行test2
    return test4  #4. 指向test4内层函数，解释器发现没有装饰器装饰本函数，所以直接运行内部函数

def test1(func):  #1. test1中的func参数全部都是now()这个方法，然后传进内部函数
    print("--开始装饰器test1--%s"%func.__name__)
    def test2():
        print("--这是装饰器2的功能--%s"%func.__name__)
        return func() #6.指向now函数并且执行now函数
    return test2  #2. 指向内部函数test2，因为解释器发现tes1又被test装饰，所以此时内部函数暂时不运行，所以test2()函数将会被当做参数传入test函数中
@test
@test1
def now():
    print("这是原函数......")

now() # 调用执行now函数
