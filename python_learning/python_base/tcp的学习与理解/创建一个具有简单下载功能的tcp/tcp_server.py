# 服务器------>提供下载的数据
from socket import *


def get_content(file_name):
    # 如果文件存在则读取文件
    try:
        with open("C:/Users/xieolei/Desktop/%s"%file_name,"rb") as f:
            content = f.read()
        return content
    except Exception as e:
        print("请求下载文件不存在")

def main():
    print("服务器已启动...")
    # 创建套接字
    server_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定地址：ip和port
    server_addr = ("192.168.253.1",8888)
    server_socket.bind(server_addr)
    # listen
    server_socket.listen(128)
    # accept
    new_client_socket,new_client_addr =  server_socket.accept()
    print("已和客户端建立连接...")
    # recv接收客户端的请求
    filename = new_client_socket.recv(1024)
    recv_filename = filename.decode("utf-8")
    print(recv_filename)
    # 获取名为filename的文件内容
    send_content = get_content(recv_filename)
    if send_content:
        # 文件内容存在，反馈给客户端
        new_client_socket.send(send_content)
        print("已经将数据发送到客户端...")
    else:
        # 文件内容不存在，结束本次客户端请求
        new_client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()