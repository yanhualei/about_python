# dict 字典
dict = {"name": "小明",
        "age": 18,
        "height": 1.75,
        "sex":"man"}

print(dict)

# 取值
print("取出key=name的value为：",dict["name"])
# print("取出索引为0的字典的key：",dict[1])

# 增加/修改键值对
# 当key不存在时，键值对才会增加，当key存在，则为修改
#增加
dict["grade"] = 3
# 修改
dict["name"] = "老王"
print(dict)
#删除
dict.pop("grade")

# 统计键值对的数量（字典的长度）
print("字典长度为：",len(dict))
# 合并键值对
print("合并前的字典为：",dict)
new_dict={"pifu":"yellow",
          "age":30}
dict.update(new_dict)
print("合并后的新字典为：",dict)

#删除字典
dict.clear()
print(len(dict))

test_list=[
    {"name":"xiaoming",
     "age":18,
     "phone":110,
     "QQ":11134},
    {"name":"laowang",
     "age":30,
     "phone":120,
     "QQ":111543212}
]
# 案例测试结果：test_list可以看做有两个元素，test_list[0]是第一个字典，test_list[1]是第二个字典
# 所以若想操作列表内的字典，i代表的是列表中的每一个字典，若想操作其中某一个特定的字典，用if控制一下即可
for i in test_list:
    if i["name"] == "xiaoming":
        print("小明的QQ是：",i["QQ"])
    if i["name"] == "laowang":
        print("老王的电话是：",i["phone"])


dic1={"name":"laowang",
     "age":30,
     "phone":120,
     "QQ":111543212}
print(dic1.values()) # 获取字典所有的值
print(dic1.keys())  # 获取字典的所有键
print(dic1.items())  # 获取字典所有的键值对