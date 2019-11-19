""""decorator装饰器：
1、什么是装饰器？
函数可以作为参数传递，增加源代码的功能，却不修改原函数的定义，这种在代码运行期间动态增加功能的方式称之为‘装饰器’
2、怎么创建装饰器？
创建装饰器代码如下面代码
3、什么情况下创建装饰器？
在需要增加某个功能模块的功能的时候
4、装饰器有什么优点?
对某个代码块进行增加功能，但是不用修改源代码块，不会影响其他地方对源代码块的正常引用

项目编程的开放封闭原则：规定已经实现的功能代码不允许被修改，但是可以被扩展"""""
def test1(func):
    def test2():
        print("--权限验证--")  #　这里增加权限验证功能
        return func  # func==>now()
    return test2  # 指向内层函数

@test1 # = now = test1(now)
def now():
    return "这是无参数函数的装饰"
# now = test1(now) # 本句为装饰器的实现原理：利用闭包函数实现对原函数重写==>一般为了增加原函数的功能
print(now()()) # 那么此时调用now函数的地方都变成了test1(now)()也就是直接运行test(now)函数



"""体验装饰器的运行过程：
# 当程序运行到@test1的时候，会自动运行到下一行，找到装饰函数，然后进行装饰
1.首先会运行@test1，也就是test1(func)模块,也就是说@test1会带着now()函数名进入test1(func)一起运行
2.test1(func) = test1(now)
3.return test2:==>test1(func)指向test2(),func指向now()
4.print(func.__name__)==>now,因为func指向的是now函数
5.运行now(),因为now=test1(now),所以这个now指向test1(func)，也就是test1(func)(),func指向now()
test1(func)指向test2，所以test1(func)()=test2()(),内函数应用外函数的参数，所以func()=now()，
func指向now，所以now()是原函数，装饰器运行完毕"""