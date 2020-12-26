
# 二分查找是基于排好序的序列
def HalfSearch(target,my_list,left,right):
    """
    :param target: 目标值
    :param my_list: 查询的列表
    :param left: 查询的初端索引
    :param right: 查询的末端索引
    :return: mid：返回目标值在列表中的位置索引
    """
    if left>right:
        return
    mid = (left+right)//2
    if my_list[mid] == target:
        return mid
    if my_list[mid]<target:
        return HalfSearch(target,my_list,mid+1,right)
    else:
        return HalfSearch(target,my_list,left,mid-1)


if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9]
    print(HalfSearch(4,my_list,0,len(my_list)-1))

"""
本段代码亲测有效！！！
如有建议或者有改进的地方敬请提出，便于共同学习！！！
有疑问的地方也可以在评论区留言！！！
"""