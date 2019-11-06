# 导入套接字
from socket import *


def main():
	# 创建套接字
	client_socket = socket(AF_INET,SOCK_STREAM)
	# 输入服务器ip和port
	server_ip = input("输入服务器ip:")
	server_port = int(input("输入服务器port:"))
	# 连接服务器
	aaa = client_socket.connect((server_ip,server_port))
	print(aaa)

	while True:
		# 发送数据
		data = input("请输入要发送的内容:")
		if data == "exit":
			break
		else:
			client_socket.send(data.encode("utf-8"))
			# 接收服务器返回的数据
			recv_data = client_socket.recvfrom(1024)
			print(recv_data[0].decode("utf-8"))
	# 关闭套接字
	client_socket.close()

if __name__ == '__main__':
	main()