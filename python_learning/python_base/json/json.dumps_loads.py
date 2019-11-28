import json
strs = {"cookie":"123456798","id":"12345677889"}

#1.json.dumps
# sort_keys:按照key的字母排序
# indent参数根据数据格式缩进显示，读起来更加清晰:
j_str = json.dumps(strs,sort_keys=True,indent=2)  # python字典类型转为json字符串
print(j_str,type(j_str))

#2.json.lods
p_str = json.loads(j_str)  # json字符串转为python字典
print(p_str,type(p_str))

#3.json.dump
f=open('temp.txt','w')
j_str2 = json.dump(strs,f,sort_keys=True,indent=2)  # python字典类型转为json字符串，并将结果存入文件f
f.close()

#4.json.load
f=open('temp.txt','r+')
p_str2 = json.load(f)  # 用于加载读取，包含json字符串格式的文本
print(p_str2)
f.close()




