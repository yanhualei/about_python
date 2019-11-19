import os
def print_directory_contents(sPath):  # 递归获取某个目录下的所有文件
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents("/home/oldeleven/PycharmProjects/about_python")