# 杨辉三角练习理解yield用法
# 公式f(n+1,m)=f(n,m)+f(n,m-1):注最大几行：H
def triangles(H):
    n, L = 0, [1]
    while n <= H:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(n)] + [1]  # 计算杨辉三角的每一行
        n += 1
for x in triangles(7):  # 输出一个7行的杨辉三角
    print(x)
