list1 = [1,4,2,6,5]
list2 = [1,2,3,6,7,8]
list3 = ['a','b2','3c','4f','1b','a7']

list1.extend(list2)  # 将列表2合并到列表1中
print(list1)
# list3= sorted(list1,reverse=False)
# print(list3)
list1.sort(reverse=False)
print(list1)

list3.sort()  # sort也可以对字符串排序,数字>字母>汉字
print(list3)



