import requests
from bs4 import BeautifulSoup
import bs4

"""BeautifulSoup主要有四类对象，Tag(标签),NavigableString(可遍历的字符串),BeautifulSoup,Comment"""
# 获取网页内容并处理
# html = requests.get("http://www.baidu.com")
# soup = BeautifulSoup(html.text)

# 获取本地文件
soup = BeautifulSoup(open("index.html","rb"),"html.parser",from_encoding="utf-8")
print(soup.prettify())  # prettify()函数是格式化打印soup对象的内容
# ---------------------------------------------------------------------------------------
# 第一个对象  Tag------>标签例如<a>、<p>、<table>、<ul>
"""Tag的name和attrs属性"""
print(soup.title)  # 打印soup内容中名为title的标签模块
print(soup.a)  # 打印soup内容中名为a的标签模块
print(type(soup.a)) # 打印soup内容中a的属性类型
print(soup.name)
print(soup.head.name)
print(soup.p.attrs)  # 打印p的所有属性(打印的是第一个p标签)
print(soup.p["class"])  # 打印p的class值
print(soup.p.get("class")) # 也是打印p的class的值
soup.p["class"] = "newclass" # 对p的值进行修改
print(soup.p)
print(soup.p.string)  # 打印p中的内容
#--------------------------------------------------------------------------------
# NavigableString(可遍历的字符串)
print(type(soup.p.string))
#--------------------------------------------------------------------------------
# Beautifulsoup
# Beautifulsoup对象表示的是一个文档的全部内容，大部分的时候
# 可以把它当做一个Tag对象，是一个特殊的Tag
print(type(soup.name)) # 打印soup的名字类型
print(soup.name)  # 打印soup的名字
print(soup.attrs)  # 打印soup的属性

#---------------------------------------------------------------------------------
# Comment
# Comment是一个特殊类型的NavigableString对象，输出的内容不包括注释符号
# 如果不好好处理，可能会对我们的文本造成意想不到的麻烦
print(soup.a)
print(soup.a.string) # a中的comment实际上是注释内容
print(type(soup.a.string))

# if type(soup.a.string)==bs4.element.Comment:
#     print(soup.a.string)  # 无法处理注释内容
for child in soup.body.children:
    print(child)  # body的孩子就是div，因此会分别输出3个div

for string in soup.stripped_strings:  # stripped_strings去除comment中空白部分
    print(string)

child = soup.title
print(child.parent.name) # 打印title标签的父节点的名字

child = soup.title.string # title的内容父节点是标签本身
print(child.parent.name)

child = soup.title.string   # 打印title内容的所有父节点
for parent in child.parents:
    print(parent.name)  # 打印结果中有document，表示的是BeautifulSoup的对象，也就是soup，表示获取的整个html文档内容
# -------------------------------------------------------------------------------------------------------------------
# 搜索文档树
 # find_all（name,attrs,recursive,text,**kgs）
print(soup.find_all("a"))  # 查找整个文档里的a标签模块
print(soup.find_all("a",class_="heima"))  # class是python的关键字，所以class后面需要添加"_"
print(soup.find_all("a",limit=3))  # 查找所有的a标签，但查找3个后就停止查找
print(soup.find_all("a",text="chuanzhi"))  # 查找文本内容是"chuanzhi"的a模块
#  find()
# find_all与find()方法唯一的区别在于：find_all()返回一个符合条件的列表
# find()直接返回第一个符合条件的结果
# ----------------------------------------------------------------------------------------------------------
# css选择器---------------->select
print(soup.select("title")) # 查找标签title的模块
print(soup.select("a.basketball"))  # 查找类选择器名为basketball的a标签模块
print(soup.select("a#book")) # 查找id选择器名为book的a标签模块
print(soup.select("ul > li > a.basketball")) # 通过子标签顺序综合查找
print(soup.select("li a[href='http://www.baidu.com']")) # 组合查找


soup =BeautifulSoup(open("index.html","rb"),"lxml",from_encoding="utf-8")
print(type(soup.select("a")))
print(soup.select("a")[0].get_text())
for a in soup.select("a"):
    print(a.get_text())  # 获取a标签下的文本内容

"""BeautifulSoup基本操作暂且就这些，更多知识有待完善"""




