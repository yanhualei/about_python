import random
class Sort:
    # 1.冒泡排序
    def maopao_sort(self,my_list):
        n = 0
        for i in range(len(my_list)-1,0,-1): # range(list,0,-1)列表list，从第零位开始，倒序
            for j in range(i):
                n = n + 1
                if my_list[j]<my_list[j+1]:
                    my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
        return my_list,n
    # 2.快速排序
    def quick_sort(self,my_list,start,end):
        if start>=end:
            return
        left = start
        right = end
        base = my_list[start]
        while left < right:
            while left < right and my_list[right] <= base:
                right = right - 1
            my_list[left] = my_list[right]
            while left < right and my_list[left] > base:
                left = left + 1
            my_list[right] = my_list[left]
            my_list[left] = base
        self.quick_sort(my_list,start,left-1)
        self.quick_sort(my_list,left + 1,end)



    # 3.归并排序
    # 4.桶排序


if __name__ == '__main__':
    my_list = random.sample(range(101),10)
    sort = Sort()

    print("---------1.冒泡排序-----------")
    result_maopao = sort.maopao_sort(my_list)
    print("排序结果：",result_maopao[0],"\n元素比较大小次数：",result_maopao[1])

    print("---------2.快速排序-----------")
    my_list2 = random.sample(range(101), 10)
    result_quick = sort.quick_sort(my_list2,0,len(my_list)-1)
    print(my_list2)

