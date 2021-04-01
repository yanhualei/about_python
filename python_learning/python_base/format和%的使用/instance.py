def func1(value):
    print('the values is %s' % value)  # %s的缺点就是value的数据类型未知，会导致未知错误


def func2(value):
    print('the values is {1},{0}'.format(value[0], value[1]))  # fotmat 的value可以是任意类型的数据和任意数量的数据


# func1((1,1))

func2((1, 2))