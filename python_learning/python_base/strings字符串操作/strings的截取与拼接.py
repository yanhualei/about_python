my_strings ='123.4567.89'

print(my_strings.split('.'))  # 将my_strings按照"."的特征来分隔

print(my_strings.split('.',1))  # 将my_strings按照"."的特征来分割，分隔一次

print("+".join(my_strings.split('.')))  # 将分隔后的字符串序列，用“+”拼接起来

# "+".join(l)  l:一定是一个iterable

