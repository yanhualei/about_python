# 操作文件和目录
# 查看当前目录的绝对路径
import os
print(os.path.abspath("testdir"))
# 在指定的目录下创建一个新目录
# os.path.join("f:/python/PycharmProjects", "testdir")
# os.mkdir("f:/python/PycharmProjects/testdir")
# 拆分路径
# print(os.path.split("f:/python/PycharmProjects/testdir"))
# 获取文件拓展名
# print(os.path.splitext("f:/python.爬虫.jpg"))
# 文件重命名
# print(os.rename("f:/python/爬虫.txt", "f:/python/test3.txt"))
# 文件删除
# os.remove("f:/python/爬虫.jpg")
# 列出当前目录的所有文件夹和文件
print([x for x in os.listdir("../")])
# 列出当前目录的所有文件
print([x for x in os.listdir() if os.path.isfile(x)])



