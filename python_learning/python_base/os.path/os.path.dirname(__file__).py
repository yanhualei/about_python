import os

# 该文件所在位置：D:\第1层\第2层\第3层\第4层\第5层\test_os.py

path1 = os.path.dirname(__file__)
print(path1)  # 获取当前运行脚本的绝对路径

path2 = os.path.dirname(os.path.dirname(__file__))
print(path2)  # 获取当前运行脚本的绝对路径（去掉最后一个路径）

path3 =os.listdir("/home/")  # 获取某个路径下的文件和文件夹
print(path3)

path6 = os.__file__  # 获取os所在的目录
print(path6)
