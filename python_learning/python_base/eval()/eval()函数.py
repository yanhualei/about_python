
# eval(source,globals=None, locals=None)
# sourse：字符串格式，是一个字符串类型的表达式或代码对象，用于做运算
# globals 用于指定运行时的全局命名空间，类型是字典，缺省时使用的是当前模块的内置命名空间。
# locals 指定运行时的局部命名空间，类型是字典，缺省时使用 globals 的值。
# 两者都缺省时，则遵循 eval 函数执行时的作用域。
# 值得注意的是，这两者不代表真正的命名空间，只在运算时起作用，运算后则销毁。
x = 10
def func():
    y = 20
    a = eval('x + y')  # 将字符串当做语句执行，返回执行结果；两者都缺省，则遵循 eval 函数执行时的作用域。
    print('a: ', a)
    b = eval('x + y', {'x': 1, 'y': 2})
    print('x: ' + str(x) + ' y: ' + str(y))  # 这两者不代表真正的命名空间，只在运算时起作用，运算后则销毁。所以x: 10 y: 20
    print('b: ', b)
    c = eval('x + y', {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    print('x: ' + str(x) + ' y: ' + str(y))
    print('c: ', c)

func()


#  eval其他常见用途
# 常见用途：将字符串转成相应的对象，例如 string 转成 list ，string 转成 dict，string 转 tuple 等等。
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(eval(a))

b = eval(a)  # eval()执行字符创a，那么a就回被当做列表执行，返回一个列表
b.append([8,8])  # 执行列表操作
print(b)


#  注意问题：eval 函数很可能会招来代码注入的问题。
#  为什么呢？ eval执行的是什么呢？ 执行的是字符串啊！