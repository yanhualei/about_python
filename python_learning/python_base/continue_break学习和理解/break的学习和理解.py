# break跳出整个循环。

for i in range(10):
    if i==5:
        break  # 当a=5时：直接结束整个循环
    print(i)

a = 0
while a<10:
    if a==5:
        break
    print(a)
    a += 1
