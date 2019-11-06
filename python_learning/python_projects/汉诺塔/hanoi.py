# 汉诺塔的游戏规则：将a上的盘子全部移到c上，大盘子不能压在小盘子上

def hanoi(n,a,b,c):  # n:盘子数量，abc分别是abc三个柱子
    """汉诺塔递归实现"""
    if n <= 0:
        return
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)  # 第一步：将a柱子上的n-1个盘子，借助c柱子，放到b柱子上
        hanoi(1,a,b,c)  #第二步：将a柱子上的最底下那个盘子，放到c柱子上
        hanoi(n-1,b,a,c)  # 第三步：将b柱子上的n-1个盘子，借助a柱子，放到c柱子上，任务完成

if __name__ == '__main__':
    hanoi(0,'A','B','C')