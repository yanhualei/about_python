def test(func):
    print("--开始装饰器test--%s"%func.__name__)
    def testa(*args,**kwargs):
        print("--这是总装饰器a的功能--%s"%func.__name__)
        return func(*args,**kwargs)  # func==>now
    return testa

def test1(func):
    print("--开始装饰器test1--%s"%func.__name__)
    def test2(*args,**kwargs):
        print("--这是装饰器2的功能--%s"%func.__name__)
        return func(*args,**kwargs)  # func==>now
    return test2
@test
@test1 # = now = test1(now)
def now():
    print("这是原函数......")
now()


"""多装饰器对同一个函数装饰执行的过程：
    1.解释器从上向下运行，当解释器遇到@test时：发现下一行不是可装饰的代码块(不是类或函数)，所以暂时不不装饰
    2.当解释器遇到test1时，解释器自动向下一行检测，发现now()是函数，可被装饰，所以开始装饰
    3.@test1 相当于 now = test1(now) ,test1(now)==>tes2,now==>test2(*args,**kwargs)  @test1装饰完毕
    4.@test开始装饰,那么@test装饰的是now()?
    @test装饰的是@test1装饰过得函数，即：
        @test
        def test2(*args,**kwargs):
            print("--这是装饰器2的功能--%s"%func.__name__)
            return func(*args,**kwargs)  # func==>now，此时now指向的是test2，即now==>test2(*args,**kwargs)，func指向的是now
    
    那么此时test2指向testa(*args,**kwargs),即：test2==>testa(*args,**kwargs)，@test装饰器装饰完毕
    5.now()函数开始运行
    然后开始运行装饰器内部的代码块：now()==>test2==>testa==>now()
    
        
    
    
"""