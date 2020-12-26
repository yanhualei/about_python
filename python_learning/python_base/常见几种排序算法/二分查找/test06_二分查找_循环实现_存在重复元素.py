
#自定义函数，实现二分查找，并返回查找结果
def binary_search(target,my_list):
    left = 0  #查找的下限
    right = len(my_list)-1  # 查找的上限
    result = []  # 保存所有查到的结果
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
            left = mid + 1  # 中间值小于目标，向右搜索，（升序序列）
        else:
            right = mid - 1  # 中间值大于目标，向左搜索
    return -1  # 未找到该元素


if __name__ == '__main__':
    my_list = [1,3,8,12, 23,22, 31, 37, 42,42,42,42, 48, 58,59]  # 升序序列
    print('目标元素在原序列的位置是：',binary_search(42,my_list))





