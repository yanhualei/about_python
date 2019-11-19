def test1(func):
    def test2(*args,**kwargs):
        print("--权限验证1--")
        print("--权限验证2--")
        return func(*args,**kwargs)
    return test2

@test1
def now(*args,**kwargs):
    sum = 0
    for i in args:
        sum += i
    print("计算结果：",sum)
    print("我的个人信息:",[(k,v) for k,v in kwargs.items() if kwargs])
"""因为now函数有两个固定参数a和b，所以传进来的参数必须>=2"""
now(1,2)
now(3,4,name="yanhualei")
"""100赋值给了a；200赋值给了b；300,400赋值给了*args；mm=1000赋值给了**kwargs"""
"""*args:是元组的方式接收传进来的参数，**kwargs：以字典的方式接收传进来的参数"""