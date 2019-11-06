# udp------>收发信息
from socket import *
from time import ctime
import threading

def send_msg(udp_socket,other_addr):
    """发送消息"""
    while True:
        data = input("请输入内容：")
        udp_socket.sendto(data.encode("utf-8"), other_addr)


def recv_msg(udp_socket):
  """接收消息"""
  while True:
    recved_msg = udp_socket.recvfrom(1024) # 每次最大接收消息容量1024
    print(ctime(),recved_msg[0].decode("gbk")) # windows编码格式是gbk，所以要用gbk方式解码


def main():
    # 创建套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    #  绑定端口
    addr = ("192.168.253.1",9999)
    udp_socket.bind(addr)  # addr是一个元组
    # 输入对方端口
    other_addr = ("192.168.253.1",8888)

   # 创建线程
    t_send = threading.Thread(target=send_msg, args=(udp_socket,other_addr)) # target线程执行目标，args目标函数需要的参数
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket, ))  # 当目标函数只需要一个参数的时候，元组内部需要一个‘逗号’，否则(udp_socket)就不是元组，而是一个普通的变量

    t_send.start()
    t_recv.start()

if __name__ == '__main__':
    main()