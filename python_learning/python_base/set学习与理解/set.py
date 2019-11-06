# 字符串统计：
# 提示用户输入任意字符串，统计字符串中每个字符出现的次数
while True:
    user_input = input("请输入任意字符串：")
    print("您输入的字符串为：", user_input)
    deal_input = set(user_input)
    for i in deal_input:
        print("%s出现了：%d次"%(i, user_input.count(i)))

# 此题解题关键：set(),合并列表中重复的元素