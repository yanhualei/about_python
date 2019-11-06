import multiprocessing
from multiprocessing import  Pool
import os
import time
#  目标
# 1.理解进程池作用和用法
# 2.完成文件复制任务，加强练习编程逻辑思维，编程习惯，纠错能力
# 3.追加复制时的进度条
# 4.如果test文件夹下不全是文件，而是还有嵌套文件夹，如何处理？（老师提示:可以考虑用递归完成）
# 5. 如果文件夹中存在压缩文件，如何实现复制任务，（自己思路:1.先解压缩，2.再递归读写）

def copy_task(filename, old_floder, new_floder,queue):

    #  想要复制文件，首先得读取源文件内容
    """

    :param filename: 文件名
    :param old_floder: 原文件夹
    :param new_floder: 新文件夹
    :param queue:  队列
    """
    f = open(old_floder + "/" + filename, "rb")
    contents = f.read()
    f.close()

    # 读取之后，将读取的内容写入新目录下的新文件里
    w = open(new_floder + "/" + filename, "wb")
    w.write(contents)
    w.close()

    queue.put(filename)
def main():
    old_floder = input("请输入要复制的文件：")
    try:
        new_floder = old_floder + "附件"
        # 创建新文件夹名字
        os.mkdir(new_floder)
    except:
        pass
    # 获取所有等待复制的文件名字
    all_old_files= os.listdir(old_floder)
    # print(all_old_files)
    # 创建进程池
    po = multiprocessing.Pool(5)
    # 创建一个队列，让复制任务和显示进度条任务进行数据交流
    queue = multiprocessing.Manager().Queue()
    # 向进程池中添加任务
    for filename in all_old_files:
        po.apply_async(copy_task, args=(filename, old_floder, new_floder,queue))
    #  结束进程池
    po.close()
    # po.join()
    # 制作进度条

    ok_copy = 0
    all_copy_file_num = len(all_old_files)
    # 获取复制成功的文件个数
    while True:
        queue.get()
        ok_copy += 1
        print("\r已经复制:%0.2f %%" % (ok_copy * 100/ all_copy_file_num),end="")
        # if queue.empty():  # 此时“已经复制:0.59 %”，可理解为queue.put = 5文件，主进程queue.get = 5个文件，此时queue队列为空，循环结束
        if ok_copy >= all_copy_file_num:
            break

if __name__ == '__main__':
    main()