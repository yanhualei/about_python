
#自定义函数，实现二分查找，并返回查找结果
def binary_search(target,list1):
    left = 0  
    right = len(list1)-1  

    while left <= right:
        mid = (left+right) // 2  
        if list1[mid]== target:
            return mid  # 返回找到的元素
        elif list1[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 未找到该元素


if __name__ == '__main__':
    my_list = [1,3,8,12, 23, 31, 37, 42,42,42,42, 48, 58]
    print('目标元素在原序列的位置是：',binary_search(42,my_list))


"""
本段代码亲测有效！！！
如有建议或者有改进的地方敬请提出，便于共同学习！！！
有疑问的地方也可以在评论区留言！！！
"""






