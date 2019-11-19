import re

"""re模块"""
# 使用match进行匹配操作
result = re.match("itcas","itcast.cn")
# 如果匹配到数据的话，用group获取数据
print(result.group())

result2 = re.match("[1-9]?\d","09")  # [1-9]?\d 意思是匹配两位数，第一位可有可无，第二位数是数字
# 但是结果是0,为什么？因为[1-9]?对“0”匹配失败，但是\d对0匹配成功，所以返回“0”
print(result2.group())

# |num 引用分组
# ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>" , "<html>hello</htmlbalabala>")
ret = re.match(r"(<[a-zA-Z]*>)(\w*)(</[a-zA-Z]*>)" , "<html>hello</htmlbalabala>")  # 给每个匹配模块加(),可用group(index)取每个模块内容
print(ret.group()) # Notype

# ret2 = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
# print(ret2.group()) # <html>hh</html>


#  (?p<name>)分组取别名
#  (?P=<name>)引用别名
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
			   "<html><h1>www.itcast.cn</h1></html>")
ret.group()
"""----------------------------------------------------------------------------------------------------------------"""
# 2 、search  搜索存在的第一个，若不存在报错Nonetype
ret =re.search(r"\d+","阅读数9999阅读数8888")# search在目标字符串中搜索，遇到第一个数字，返回结果并结束，不在搜索
print(ret.group())  # 9999

# 3、findall 查找所有  若不存在返回空字符串  没有group()方法
ret = re.findall(r"阅读数(.*?)阅读数(\d+)阅读数\d+","阅读数9.9.9.9阅读数8888阅读数7777")  # findall在目标字符串中查找，查找到的结果，以一个列表形式返回
print(ret)  # re.findall:如果匹配规则中有group那么结果只会返回group中匹配的结果


# 4、sub 替换  没有group()方法
# re.sub(r"\d+","替换者"，"被替换者")
ret = re.sub(r"\d+", "999", "python=888")
print(ret) # python=999  999的位置也可以是一个变量，接收函数返回值


# split
ret = re.split(r":| ","info:xiaoZhang 33 shandong")  # 用"："或者"空格"分割目标字符串
print(ret)


# re.compile:要求获得ip:port
s  =""""<ul class="l2">
		    	<span><li>111.29.3.194</li></span>
		        <span style="width: 100px;"><li class="port GEGEA">8877</li></span>
				<span style="width: 100px; color:red;"><li>高匿</li></span>
				<span style="width: 100px;"><li>http</li></span>
		        <span><li>中国</li></span>
		        <span style="width: 200px;"><li>海南海口</li></span>
		        <span style="width: 100px;"><li>移动</li></span>
		        <span style="width: 100px;"><li>0.444 秒</li></span>
		        <span style="border:none; width: 190px;"><li>1分钟前</li></span>
		        <div class="clearfix"></div>
		    </ul>"""
com = re.compile("<span><li>(.*?)</li></span>\s+<span .*?><li .*?>(\d+)</li></span>",re.M)
print(com.findall(s))
