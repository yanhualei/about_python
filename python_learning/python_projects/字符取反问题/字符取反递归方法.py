
my_back_list = []  # 定义一个新列表，保存反转结果
def out_put(my_list,length):
    if length == 0:
        return
    my_back_list.append(my_list[length-1])
    if length-1 == 0: #获取列表最后一次数据时，再输出结果
        print(my_back_list)
    out_put(my_list, length-1)







if __name__ == '__main__':
    strs = input("请输入字符串")
    my_list = []
    for i in strs:
        my_list.append(i)

    length = len(my_list)
    out_put(my_list,length)
