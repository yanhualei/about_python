# 二分查找（递归实现）（可查找重复元素）
def HalfSearch(target,my_list,left,right):
    if left >right:
        return
    mid = (left + right)//2
    result = []  # 存储序列中所有目标元素的索引

    if my_list[mid] == target:
        result.append(mid)
        l = mid
        while True:
            if my_list[l-1] == target: # target目标元素向左搜索
                result.append(l-1)  # 存在就存储到result列表中
                l = l-1 # 继续向左搜索
            else:
                break  # 不存在就退出循环
        result.reverse()  # 向左搜索是倒序的，所以需要反转顺序

        r = mid
        while True:
            if my_list[r+1] == target:  # target目标元素向右搜索
                result.append(r+1)
                r = r+1
            else:
                break
        return result
    if my_list[mid] <= target:
        return HalfSearch(target,my_list,mid+1,right)
    else:
        return HalfSearch(target,my_list,left,mid-1)


if __name__ == '__main__':
    my_list = [1,2,3,4,4,5,6,7,9]
    print("目标元素在原序列的位置是：",HalfSearch(4,my_list,0,len(my_list)-1))


    '''
    代码亲测有效！！！
    二分查找我就不赘叙了，这段（可查找重复元素的二分查找）算法是
    在原二分查找算法基础上添加了两个循环实现了可查找重复元素的二分查找
    如有建议或者有改进的地方敬请提出，便于共同学习！！！
    有疑问的地方也可以在评论区留言！！！
    '''
