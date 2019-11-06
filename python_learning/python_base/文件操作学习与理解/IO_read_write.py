# 读写文件的学习与理解
import time


def read_file():
    with open("read_test.txt", "r+") as f:  # 读取完成自动关闭读取操作
        # print(f.read())  # 一次性全部读取，对已知的小文件可以直接全部读取，若是大型文件，就是卡爆内存
        while True:
            datas = f.readline()
            yield datas
            if datas == '':
                break
    # print(type(datas))
        # print("发送数据",len(datas))



def write_file(datas):
    # print("接受数据：",len(datas))
    with open("write_test.txt", "a+") as f:  # 创建文件，文件存在就覆盖
        f.writelines(datas)

if __name__ == '__main__':

        # print(type(datas))
        # print(len(datas))
    while True:
        datas = read_file()  # 将读取到的数据变成生成器对象，节省内存
        write_file(datas)


    # print(f.readlines())  # 一次读取所有行内容并按行返回list
    # for line in  f.readlines():
    #     print(line.strip())
    #如果文件很小，直接read()最方便，如果不能确定，可反复调用read(size)，每次调用固定大小的文件内容
    # 如果是配置文件，调用readlines()最方便

# #读取二进制文件（图片，视频等二进制文件需要用"rb"读取）
# with open("f:/python/爬虫.jpg","rb") as g:
#     print(g.read())

# with open("f:/python/test2.txt", encoding="gbk") as gbk:
#     print(gbk.read())


# r 打开只读文件，该文件必须存在，不存在会报错。
# r+ 打开可读写的文件，该文件必须存在，不存在会报错。
# w 打开只写文件，文件不存在，新建文件；文件存在，覆盖原文件
# w+ 打开可读写文件，文件不存在，新建文件；文件存在，覆盖原文件
# a 以附加的方式打开只写文件。文件不存在，新建文件；文件存在，追加写入
# a+ 以附加方式打开可读写的文件。文件不存在，新建文件，文件存在，追加写入
# wb 在windows下，以二进制进行存储，\r\n才是换行
# w 是以文本方式进行存储\n是换行
# rb 取出来的也是\r\n
# r取出来的是\n

# file.write(str)的参数是一个字符串，就是你要写入文件的内容.
# file.writelines(sequence)的参数是序列，比如列表，它会迭代帮你写入文件。