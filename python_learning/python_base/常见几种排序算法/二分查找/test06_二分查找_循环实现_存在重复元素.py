
#自定义函数，实现二分查找，并返回查找结果
def binary_search(target,my_list):
    left = 0
    right = len(my_list)-1
    result = []
    while left <= right:
        mid = (left+right) // 2  # 中间值
        if my_list[mid]== target:
            result.append(mid)
            l = mid  # target目标元素向左搜索
            while True:
                if my_list[l - 1] == target:
                    result.append(l - 1)
                    l = l - 1
                else:
                    break
            result.reverse()
            r = mid  # target目标元素向右搜索
            while True:
                if my_list[r + 1] == target:
                    result.append(r + 1)
                    r = r + 1
                else:
                    break
            return result
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 未找到该元素


if __name__ == '__main__':
    my_list = [1,3,8,12, 23, 31, 37, 42,42,42,42, 48, 58]
    print('目标元素在原序列的位置是：',binary_search(42,my_list))





