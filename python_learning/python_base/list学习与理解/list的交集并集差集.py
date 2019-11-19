
# 思路：将列表转换成集合，然后在求交并差
a=[1,2,3,4,5]
b=[3,6,5,7,4,2]

# 交集
jj=list(set(a).intersection(set(b)))
print(jj)
# 并集
bj = list(set(a).union(set(b)))
print(bj)
# 差集
cj = list(set(a).difference(set(b)))
print(cj)