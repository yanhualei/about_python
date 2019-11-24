M = [[1,2,3],[4,5,6],[7,8,9]]
N = [[2,2,2],[3,3,3],[4,4,4]]

# 求M,N两个矩阵的积
result1 = [M[row][col]*N[row][col] for row in range(3) for col in range(3)]
result2=[[M[row][col]*N[row][col] for col in range(3)] for row in range(3)]
result3 =[[M[row][col]*N[row][col] for row in range(3)] for col in range(3)]
print(result1,'\n',result2,'\n',result3)