# 快速排序
# 1.定义两个指针，left和right分别指向列表的start和end
# 2.定义基准值，一般为列表第一位元素，base = list(start)
# 3.右边开始排序，大于基准值，就将该元素放到左边序列
# 4.左边开始排序，小于基准值，就将该元素放到右边序列
# 5.当left=right时，本次排序结束，基准值放到list(left)=mid
# 6.递归排序左边
# 7.递归排序右边

# 快排思想：快排之所以快，是使用了分治思想，什么是分治思想呢？
# 将一个难以直接解决的大问题，分割成一些规模较小的相同问题，以便各个击破，分而治之，也就是分别解决


import random


def quick_sort(my_list, start, end):
    if start >= end:  # 递归结束条件
        return
    left = start  # 左指针
    right = end  # 右指针
    base = my_list[start]  # 基准值
    while left < right:
        while left < right and my_list[right] <= base:  # 基准值右边序列与基准值比较,left < right这个条件保证了右指针探测的结束条件
            right -= 1
        my_list[left] = my_list[right]  # 将右指针探测出来小于基准值的值保存到当前左指针处
        while left < right and my_list[left] > base:  # 基准值左边的序列与基准值比较，left < right这个条件保证了左指针探测的结束条件
            left += 1
        my_list[right] = my_list[left]  # 将左指针探测出来的大于基准值保存到当前右指针处，那么此时就形成了大于基准值和小于基准值的两个数的位置互换
    my_list[left] = base  # 左右两边比较互换完成之后，也就是left=right时候：左右指针到达了相同位置，将基准值放到当前位置
    quick_sort(my_list, start, left - 1)  # 基准值左边递归排序
    quick_sort(my_list, right + 1, end)  # 基准值右边递归排序


if __name__ == '__main__':
    my_list = random.sample(range(2000000), 1000000)  # 从0-1999999中随机取出1000000个数据，并且返回
    quick_sort(my_list, 0, len(my_list) - 1)
    print(my_list)
