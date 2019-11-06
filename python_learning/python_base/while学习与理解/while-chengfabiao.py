# 制作9*9乘法表
def fun_multify(m):
    row = 1  # 从第一行开始
    while row <= m:  # 设定行数9行
        col = 1  # 从第一列开始
        while col <= row:  # 控制每列打印的元素数
            print("%d*%d=%d"%(col, row, col*row), end="\t")  # 打印元素，结尾制表方式排列，不换行
            col += 1  # 列+1
        print("")  # 换行
        row += 1  # 行+1

fun_multify(10)