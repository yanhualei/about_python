import os
def print_directory_contents(sPath):  # 递归获取某个目录下的所有文件
    for sChild in os.listdir(sPath):  # listdir：列出当前文件夹内的文件和文件夹
        sChildPath = os.path.join(sPath,sChild) # 文件和文件夹拼接完整路径
        if os.path.isdir(sChildPath):  #isdir：只有文件的完整路径才能判断
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents("/home/oldeleven/PycharmProjects/about_python")