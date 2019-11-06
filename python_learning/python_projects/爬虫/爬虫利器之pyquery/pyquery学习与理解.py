# 爬虫利器二--------->PyQuery
from pyquery import PyQuery as pq
import requests

# pyquery 的基本操作

"""
    1..html()和.text():获取相应的html模块和文本模块
    2. ("selector"):通过选择器来获取相应的目标内容
    3. .eq(index):根据索引来获取指定元素
    4. .find():查找嵌套元素
    5. .filter():根据class、id帅选指定元素
    6. .attr():获取、修改属性值
    7. .addClass(value):添加类选择器
    8. .hasClass(name):判断是否有指定的类选择器，有返回True，否则返回False
    9. .children():获取子元素
    10. .parents():获取父元素
    11. .next(): 获取下一个元素
    12. .nextAll():获取后面全部元素块
    13. .not_("selector"):获取所有不与该选择器匹配的元素
    14. for i in d.items("li"):print i.text():遍历d中li模块中的文本内容
"""

deal_html = pq(filename="index.html")  # 将inex.html传入pyquery工具包
# print(type(get_html))
# print(deal_html.text())
print(deal_html("a"))
print(deal_html(".basketball"))
print(deal_html("#football"))
div = deal_html(".div1")  # 获取选择器为".div1"的div
for li in div.items():  #
    a2 = li("a").eq(2).text()
    print(a2)
test = div.items()
print(type(div.items()))

