# 导入套接字
from socket import *
def main():
    # 创建套接字
    server_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定ip和port：注意：绑定的地址是一个元组
    addr = server_socket.bind(("",9999))# ip不写的情况，默认代表的是本机127.0.0.1
    # listen
    server_socket.listen(128) # listen 不堵塞，只是将套接字变为被动链接
    while True:
        # 当有客户端连接进来 accept解阻塞，分配服务
        print("为一个新客户端服务...")
        new_client_socket,client_sddr = server_socket.accept()
        while True:
            # 接收消息
            data = new_client_socket.recv(1024)
            #recv()解堵塞有两种情况
            #1、客户端关闭，客户端会返过来空值，recv()也会解堵塞
            #2、客户端发来数据，recv()解堵塞
            if data: # 如果是客户端关闭，data=none，data is false,如果data是客户端发来数据，data is true
                print("客户端的请求是...")
                print(data.decode("utf-8"))
                # 反馈消息
                send_data ="server:您的消息已收到..."
                new_client_socket.send(send_data.encode("utf-8"))
            else:
                print("客户端已下线，结束服务...")
                break
        new_client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()