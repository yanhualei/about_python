# 归并排序
import random


def merge_sort(my_list):
    if len(my_list)<=1:
        return my_list
    mid = len(my_list)//2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
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

if __name__ == '__main__':
    my_list = random.sample(range(1000),10)
    result = merge_sort(my_list)
    print(result)
