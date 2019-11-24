#生成器是一个特殊的迭代器,节省内存空间，因为生成器保存的不是数据而是生成数据的方式
# 普通方法完成斐波拉契数列1,1,2,3,5,8,13,21,34.....
def fib( len ):
    n = 0
    a = 0
    b = 1
    L = [1]
    while n < len:
        a, b = b, a+b
        n += 1
        L.append(b)
    print(L)
fib(9)

def fib2(max):
    n, a, b = 0,0,1
    print("-----1------")
    while n<max:
        print("-----2------")
        yield  b  # 如果一个函数中存在yield，那么此函数不再是函数，而是一个生成器模板
        print("-----3-----")
        a,b = b,a+b
        n+=1
        print("-----4-----")

obj = fib2(10)  # 如果在调用fib2的时候，发现此时函数中有yield，那么此时不是在调用函数
# 而是创建生成器对象
for x in obj:
    print(x)



