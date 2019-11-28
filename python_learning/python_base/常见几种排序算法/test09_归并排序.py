# 归并原理参考http://yshblog.com/blog/171
import cProfile
import random


def merge_sort(my_list):
    """列表二分分解"""
    if len(my_list) <= 1:
        return my_list
    mid = len(my_list)//2  # 不能整除2，防止传进来的列表长度是个奇数
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    # 合并
    return merge(left,right)
    # print(left,right)

def merge(left,right):
    """合并操作,将两个有序数组left和right合并成一个大的有序数组"""
    # left和right的下标指针
    l, r = 0, 0
    # 最终的排序结果
    result = []

    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

# my_list = random.sample(range(2000000), 1000000)  # 从0-1999999中随机取出1000000个数据，并且返回
my_list = [4,5,9,2,1]
result = merge_sort(my_list)
print(result)

# print(cProfile.run("merge_sort(my_list)"))


# 时间复杂度
# 最优时间复杂度：O(nlogn)
# 最坏时间复杂度：O(nlogn)
# 稳定性：稳定

