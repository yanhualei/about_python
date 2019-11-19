list1 = [1,4,2,6,5]
list2 = [1,2,3,6,7,8]

list1.extend(list2)  # 合并两个列表
# list3= sorted(list1,reverse=False)
# print(list3)
list1.sort(reverse=False)
print(list1)