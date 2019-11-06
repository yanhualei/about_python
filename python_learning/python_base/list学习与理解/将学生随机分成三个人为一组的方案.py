import random
l = [x for x in range(1,101)]  # 生成列表
random.shuffle(l)  # 将列表l顺序打乱  注：random.shuffle(l)返回值为None,他是直接在原列表上打乱顺序
y = [l[i:i+5] for i in range(0,100,5)]  # 切片

print(y)


# 实现将全班学生100个按照学号随机分成5组