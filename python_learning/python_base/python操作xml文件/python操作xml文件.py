# 使用xml.dom解析xml
# 文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。
#
# 一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。
#
# python中用xml.dom.minidom来解析xml文件，实例如下：
# import xml.dom.minidom
from xml.dom.minidom import parse

DOMTree = parse("movies.xml")  # 解析xml文件

# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print("Root element : %s" % collection.getAttribute("shelf"))
movies = DOMTree.getElementsByTagName("movie")  # 直接通过标签名获取Elements，getElementsByTagName返回列表
for movie in movies:
   name = movie.getElementsByTagName('name')[0]  # 获取type的Elements
   datas = name.childNodes[0].data  # 为什么不是type.data,记住标签之间的文本也是一个节点
   attri = movie.getAttribute("title")
   movie.setAttribute("title","hellow")
   print(attri)