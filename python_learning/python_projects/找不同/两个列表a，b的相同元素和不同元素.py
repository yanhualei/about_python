a = [1,2,3,4,5,6,7,8,9]
b = [1,3,5,7,9,4,3,12,11,15]

print(set(a)&set(b))  # ab都有的元素  交集
print(set(a)^set(b))  # ab不同的元素  非交集部分
print(set(a)|set(b))  # ab合并到一起  并集