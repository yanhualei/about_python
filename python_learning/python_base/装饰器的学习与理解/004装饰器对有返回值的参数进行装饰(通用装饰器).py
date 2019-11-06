def test1(func):
    def test2(*args,**kwargs):
        print("--权限验证1--")
        print("--权限验证2--")
        return func(*args,**kwargs) # 添加return和不定长参数==>通用装饰器
    """1.*args：以元组的方式对参数进行拆包
        1.1：原函数有定长参数==>a,b 如果传进来的参数个数n=2，
             那么这两个参数会分别赋值给a和b，
       2：以字典的方式对参数进行拆包
        2.1：如果传进来带有mm=1000这种形式的参数，即关键字参数，这种参数将会赋值给**kwargs
    """

    return test2

@test1 # = now = test1(now)
def now(a,b,*args,**kwargs):
    print("%d,%d"%(a,b))
    print(args)
    print(kwargs)
    return "ok？"
"""因为now函数有两个固定参数a和b，所以传进来的参数必须>=2"""
now(100,200)
now(100,200,300)
now(100,200,300,400,mm=1000)
"""100赋值给了a；200赋值给了b；300,400赋值给了*args；mm=1000赋值给了**kwargs"""
"""*args:是元组的方式接收传进来的参数，**kwargs：以字典的方式接收传进来的参数"""