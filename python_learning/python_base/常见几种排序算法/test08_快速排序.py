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
    """
    快排递归方法
    :param my_list:
    :param start:
    :param end:
    :return:
    """
    if start >= end:  # 递归结束条件
        return
    left = start  # 左指针
    right = end  # 右指针
    base = my_list[start]  # 基准值
    while left < right:
        my_list[left] = my_list[right]
        while left < right and my_list[left] > base:  # 基准值左边的序列与基准值比较，left < right这个条件保证了左指针探测的结束条件
            left += 1
        my_list[right] = my_list[left]  # 将左指针探测出来的大于基准值保存到当前右指针处，那么此时就形成了大于基准值和小于基准值的两个数的位置互换
    my_list[left] = base  # 左右两边比较互换完成之后，也就是left=right时候：左右指针到达了相同位置，将基准值放到当前位置
    quick_sort(my_list, start, left - 1)  # 基准值左边递归排序
    quick_sort(my_list, right + 1, end)  # 基准值右边递归排序


def quick_sort2(qlist):
    """
    方法二
    :param qlist:
    :return:
    """
    if qlist == []:
        return qlist
    base = qlist[0]
    qlittle = quick_sort2([l for l in qlist[1:] if l<base])  # 小于base的一边独自递归排序
    qbig = quick_sort2([b for b in qlist[1:] if b>=base])  # 大于base的一边独自递归排序
    return qlittle + [base] + qbig  # 左右两边排序玩了返回排序后的列表


# 一句代码实现快排
# 选择第一个元素当参考值
# 小于参考值的放左边
# 大于参考值的放右边
quick_sort3 = lambda array:array if len(array)<=1 else quick_sort3([l for l in array[1:] if l<array[0]])\
+ [array[0]] + quick_sort3([r for r in array[1:] if r>=array[0]])


def quick_sort4(array, l, r):
    if l >= r:
        return array

    stack = []  # 定义一个空的列表形式的栈
    stack.append(l)  # 向栈添加序列的最左端索引
    stack.append(r)  # 添加右端索引
    while stack:
        low = stack.pop(0)  # 获取左部分
        high = stack.pop(0)  # 获取右部分
        if high-low <= 0:
            continue
        base = array[high] # 取最右端的元素作为轴
        i = low - 1  # 标记点，用于标记小于轴值的栈位置，肯定有人会问为什么要减一，我们可以不减一试一下，接着看下面代码
        # 第一次比较，4<=5吗？是的，那么它应该位置不变对吧，它应该跟自己交换位置，但是此时i=1,j=0,肯定不对的，所以i的初始值要序列起始位置基础上-1
        for j in range(low,high):  # 遍历当前数据段的元素
            if array[j] <= base:  # 如果元素小于等于轴值
                i += 1 # 标记点向后移动一位
                array[i],array[j] = array[j],array[i]  # 交换标记点和当前元素的位置
        array[i+1],array[high] = array[high],array[i+1] # 本次所有元素都和轴值比较完毕，将轴值插入标记点的后面，那么此时序列轴值左边的元素都小于轴值，右边元素都大于轴值
        stack.extend([low,i,i+2,high])  # 将左区间元素，和右区间的元素加入栈中，其实[low,i]，[i+2,high]又是两个新列表


if __name__ == '__main__':
    qlist = random.sample(range(200000), 50000)  # 从0-1999999中随机取出1000000个数据，并且返回
    # quick_sort(my_list, 0, len(my_list) - 1)
    # print(my_list)

    # 快排方法2
    # qlist = [4, 5, 6, 7, 3, 2, 6, 9, 8]
    print(quick_sort2(qlist))

    # 方法三：
    print(quick_sort3([3, 8, 4, 6, 7, 1]))

    # 方法四：
    list = [4, 3, 1, 9, 8, 6, 5]
    quick_sort4(list, 0, len(list) - 1)
    print(list)