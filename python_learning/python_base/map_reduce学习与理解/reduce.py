# map/reduce理解与练习
# 基本概念：map接收一个函数和一个序列，该函数分别作用于每一个序列元素；map(函数，序列)
#           map的函数可接收一个或多个参数
#           reduce接收一个函数和一个序列，该函数与传入序列的第一个元素作用得到结果后，
#           将结果继续与下一个元素继续发生关系
#           reduce函数只能接收2个参数
# 利用map与reduce得到一个list内部元素的积
# 测试案例1:[3,5,7,9]--->945
# 测试案例2:[2,4,6,8]--->348
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x+y,L)# reduce作用于序列的所有元素

# lambda x,y:x*y:此语句表示两个参数的乘积，并且返回乘积结果

print(prod([2,4,6,8]))
















