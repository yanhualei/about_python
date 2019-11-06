
# 普通版本：序列中不能存在负数和小数
import random

# 1.利用max和min函数找出序列中最大值和最小值---->以便于算出桶的个数
# 2.创建桶
# 3.遍历桶，循环桶内的元素

def bucket_sort(my_list):
    # 最大值和最小值
    _min = min(my_list)
    _max = max(my_list)
    bucket_len = _max - _min + 1
    bucket_list = [0 for i in range(bucket_len)]
    # 装桶
    for i in my_list:
        bucket_list[i-_min] += 1
    # 遍历桶
    n = 0
    current = _min
    for j in bucket_list:
        while j > 0:
            my_list[n] =current
            j -= 1
            n += 1
        current +=1
    return my_list

if __name__ == '__main__':
    # my_list = random.sample(range(10000000),5000000)
    my_list = [6,4,8,5,5,9]
    result = bucket_sort(my_list)
    print(result)
