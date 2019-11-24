from collections import Iterable
# filter:过滤，返回包含过滤的值的一个可迭代对象
# 下面过滤筛选奇数偶数
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fun(p):
    return p%2 ==1
result = filter(fun,a)  # 将a序列中的每个元素传递到fun中，返回过滤结果
print(type(result))
print(isinstance(result,Iterable))
# print([i for i in result])
print(list(result))