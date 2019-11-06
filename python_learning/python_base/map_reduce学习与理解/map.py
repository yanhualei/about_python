from collections import Iterable
def prod(L):
    return map(lambda x:x**2,L)  # map作用于序列L中的每一个元素，返回值是一个Iterable，可迭代对象

# lambda x,y:x*y:此语句表示两个参数的乘积，并且返回乘积结果
m = prod([2,4,6,8])

# print(isinstance(m,Iterable))

print(list(m))