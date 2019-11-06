# 打印一个等腰三角形(1,3,5,7,9),a1+(n-1)-->列跟行的关系是2n+1


def eq_trangle(x):
    row = 1
    while row <= x:  # x确定要打印的最大行数
        i = 1
        while i <= x-row:  # 关键：找出最大行数与列之间的关系
            print(" ",end="")
            i += 1
        col = 1
        while col <= 2*row-1: # 关键：找出行和列之间的关系
            print("*",end="")
            col += 1
        row += 1
        print("")

eq_trangle(10)  #最大行设置为10


