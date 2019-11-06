# 客户端----->下载
from socket import *
import time


def main():
    # 创建套接字
    client_socket = socket(AF_INET,SOCK_STREAM)
    # 输入服务器ip和port
    server_addr = ("192.168.253.1",8888)
    # 连接服务器
    client_socket.connect(server_addr)
    print("成功连接服务器")
    # 向服务器发送请求
    # 请求是:下载一个文件
    filename = input("请输入要下载的文件名称:")
    client_socket.send(filename.encode("utf-8"))
    # 接收服务器反馈的信息
    recv_data = client_socket.recv(1024)
    print(recv_data.decode("gbk"))
    # 如果文件存在，将接收的数据写在一个文件里，完成下载功能
    if recv_data:
        with open("[新]%s"%filename,"wb") as f:  # 在当前目录下创建文件，然后完成写操作
            f.write(recv_data)
            print("文件下载完成")

    else:
        # 关闭套接字
        print("文件下载失败")
        client_socket.close()


if __name__ == '__main__':
    main()