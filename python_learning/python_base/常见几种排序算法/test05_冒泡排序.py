# 冒泡算法
"""
算法思想：每个元素与后面的元素比较，比较大的放在前面
"""
import random


def maopao(num_list):
    """

    :param num_list: 需要排序的元素序列
    :return:
    num_list:完成排序的列表
    n:完成排序所需的次数
    """
    n = 0
    for i in range(len(num_list)-1,0,-1):  #range(list,0,-1)列表list，从第零位开始，倒序
        for j in range(i):
            n = n +1
            if num_list[j] < num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1],num_list[j]
    return num_list,n

if __name__ == '__main__':
    num_list = random.sample(range(2000000),1000000)
    result= maopao(num_list)
    # print(type(result))
    print("排序结果：",result[0],"\n元素比较大小次数：",result[1])
