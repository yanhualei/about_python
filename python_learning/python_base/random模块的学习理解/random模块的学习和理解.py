import random

my_list = [0,1,2,3,4,5]

print("随机一个0-1之间的浮点数：%.2f"%random.random())
print("随机一个整数：%d"%random.randint(0,9))
print("随机一个浮点数：%.2f"%random.uniform(1,9))
print("随机取一个序列：",random.sample(my_list,5))
print("随机取一个元素：",random.choice("testpython"))
random.shuffle(my_list)
print("随机打乱一个序列",my_list)
