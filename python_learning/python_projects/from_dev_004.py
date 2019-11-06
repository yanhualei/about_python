# 二分查找
def half_search(target,my_list):
    start = 0
    end = len(my_list)-1
    while start <= end:
        mid = (start + end) // 2
        if my_list[mid] == target:
            return mid
        if my_list[mid] <= target:
            start = mid
        if my_list[mid] > target:
            end = mid

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9]
    target =6
    result = half_search(target,my_list)
    print(result)