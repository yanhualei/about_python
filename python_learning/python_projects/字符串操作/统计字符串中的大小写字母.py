# 统计一个字符串中大小写字母的数量

strs = "I Love Python!"
my_list = []
for i in strs:
    if i.isalpha():
        my_list.append(i)
print([upword for upword in my_list if upword.isupper()])
print([upword for upword in my_list if upword.islower()])