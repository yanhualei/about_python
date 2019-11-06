# 元组
# 定义空元组
tup1 = ()
print("()的类型为：",type(tup1))
tup = (3,)  # 注意不能写成，tup = (3),否则tup就不是一个元组，而是tup = 3
print("(3,)的类型为：",type(tup))

# 查询元组元素
tup_1 = (1,2,4,3,5,2,6)
print("索引为0的元组元素为：",tup_1[0])
print("元素为4的索引为：",tup_1.index(4))
print("元素2在tup_1中出现的次数为：", tup_1.count(2))
print("元组tup_1的长度(元素个数)为:",len(tup_1))
# 分别取出tuple中的每个元素,由列表接收
L1 = []
for i in tup_1:
    L1.append(i)
print("取出tup_1的所有元素为：",L1)


# 将元组转换为列表
# 方法一
list_tup = list(tup_1)
print("tup_1转化为list结果为：",list_tup)
# 方法二
L = []
for lis in tup_1:
    L.append(lis)
print("tup_1转化为list结果为：",L)

# 将列表转化为元组
lis_tup = tuple(L)
print("L列表转化为元组lis_tup为：",lis_tup)

