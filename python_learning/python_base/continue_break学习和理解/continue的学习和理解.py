# Python continue 语句跳出本次循环，而break跳出整个循环。
#
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
#
# continue语句用在while和for循环中。

for i  in range(1,10):
    if i ==5:
        continue  # 当i=5时：跳过下面代码，直接进入下一次循环
    print(i)

a = 0
while a<10:
    a += 1
    if a==5:
        continue  # 当a=5时：就不执行print(a),进入下一次循环
    print(a)