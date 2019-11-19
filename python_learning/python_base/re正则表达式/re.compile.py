# re.compile 函数
# re.compile是将正则表达式编译成一个对象，加快速度，并重复使用
import re

# re.compile:要求获得ip:port
html  =""""<ul class="l2">
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
com = re.compile("<span><li>(.*?)</li></span>\s+<span .*?><li .*?>(\d+)</li></span>",re.M)  # re.M：多行模式
print(com.findall(html))
print(com.match(html))  # 因为match是从字符串的第一个字符开始匹配，所以在本例中匹配为空None
print(com.search(html).group(1)+":"+com.search(html).group(2))  # search是在字符串中寻找，第一次遇到的字符串返回结果并结束，不在搜索
# 我们这里用()标注我们要的结果，方便我们取操作