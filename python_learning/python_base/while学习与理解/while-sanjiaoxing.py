# 创建三角形
# 一号三角形
print("(1)")
row=1
while row <= 9:
    col=1
    while col <= row:
        print("*",end="\t")
        col+=1
    print("")
    row += 1

print("\n")  # 图形隔开

# 一号三角形水平方向旋转180°
print("(2)")
row=1
while row <= 9:
    col = 1
    while col <= 10-row:
        print("*",end="\t")
        col+=1
    print("")
    row += 1
print("\n")  # 图形隔开

#一号三角形垂直方向旋转180°
print("(3)")
row = 1
# 控制行数
while row <= 9:
    i = 1
# 打印空白部分
    while i <= row-1:  # row-1,去掉每行第一列的空白
        print(" ", end="\t")
        i += 1
    col = 1
# 打印星星部分
    while col <= 10 - row:
        print("*", end="\t")
        col += 1
    print("")
    row += 1

print("\n")  # 图形隔开


# 3号三角形水平方向折叠
print ("(4)")
row = 1
while row <= 9:
    i = 1
    while i <= 9-row:
        print (" ",end="\t")
        i += 1
    col = 1
    while col <= row:
        print("*",end="\t")
        col += 1
    print("")
    row += 1


