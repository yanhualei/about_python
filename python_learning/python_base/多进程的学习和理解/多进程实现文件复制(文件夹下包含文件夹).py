import multiprocessing
import os
import time
import threading


def show_copyfile(file_name):
    print('\r已经完成拷贝：%s' % file_name, end="")

def show_copyprocess(copy_ok,all_file):
     print("\r已经复制文件：%0.2f%%"%(copy_ok *100/all_file),end="")

def copy_task(old_folder_name, new_folder_name, file_name,queue):
    # 读取源文件内容
    # print(file_name)
    with open(old_folder_name + "/" + file_name, "rb") as r:
        content = r.read()
    # 写入新文件
    with open(new_folder_name + "/" + file_name, "wb") as w:
        w.write(content)

    queue.put(file_name)
def main():
    # 输入即将拷贝的文件名字
    old_folder_name = input("请输入源文件名字:")
    # 创建新文件
    try:  # 创建的文件有可能已经存在
        new_folder_name = old_folder_name+"附件"
        os.mkdir(new_folder_name)
    except:  # 如果已经存在，忽略错误，继续运行
        pass

    # 获取所有等待复制的文件名字
    all_file_list =  os.listdir(old_folder_name)
    print(all_file_list)
    # 创建进程池
    po = multiprocessing.Pool(5)
    # 创建一个队列，让复制任务和进度条进行数据交流
    queue = multiprocessing.Manager().Queue()
    # 向进程池中添加任务
    for file_name in all_file_list:
        po.apply_async(copy_task,args=(old_folder_name,new_folder_name,file_name,queue))
    # 任务添加完毕，结束进程池
    po.close()
    # po.join()  # 主进程等待进程池中所有任务完成

    # 利用线程，让正在被复制的文件，和复制百分比分别同时显示

    copy_ok = 0  # 已经完成复制的文件
    all_file= len(all_file_list)  # 总文件个数
    while True:
        copy_ok += 1
        file_name = queue.get()
        show_copyprocess(copy_ok,all_file)
        # 什么时候才算复制完呢
        if copy_ok >= all_file:
            break

if __name__ == '__main__':
    main()

