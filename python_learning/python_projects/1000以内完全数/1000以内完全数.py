# 1000以内的完全数：6=1+2+3，完全数=因子之和



def perfect_number():
    """1000以内的完全数"""
    # 1、求因子
    l = [] # 定义列表存放因子
    sum = 0
    for i in range(2,1000):
        for j in range(1,i):
            if i%j == 0:
                l.append(j)
        for k in l:
            sum += int(k)  # 求出因子之和
        if i ==sum:  # 如果这个数=因子之和，就输出
            print(i,l)

        sum = 0  # 初始化sum
        l.clear() # 初始化 l



if __name__ == '__main__':
    # strs = int(input("请输入数字：\t"))
    perfect_number()

