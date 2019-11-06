import socket
import re


def service_client(new_client_socket):
    # 接收客户端发来的请求
    request = new_client_socket.recv(1024).decode("utf-8")
    # print(requset)
    # 反馈给客户端相应数据
    # header
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "\r\n"
    # body
    # 返回服务器相关页面内容
    req_list = request.splitlines()  # 按行分隔，返回列表
    print(req_list)
    # 获取客户端请求的资源路径
    ret = re.match(r"[^/]+(/[^ ]*)",req_list[0])
    print(ret.group(1))
    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":  # 只输入ip:port的情况下，即：只输入网址的情况下，默认指向主页
            file_name = "/index.html"
    # 读取路径下的文件
    try:
        f = open("./web" + file_name,"rb")  # 可能客户顿请求的资源页面不存在
    except:   # 如果请求页面不存在  返回error_404页面
        file_name = "/error_404/error_404.jpg"
        response_error_header = "HTTP/1.1 200 OK\r\n"
        response_error_header += "\r\n"
        with open(r"./web" + file_name, "rb") as error:
            response_error_body = error.read()
        new_client_socket.send(response_error_header.encode("utf-8"))
        new_client_socket.send(response_error_body)
    else:  #kk 如果客户端请求资源页面存在，读取内容并且返回给客户端
        response_body = f.read()
        f.close()
        new_client_socket.send(response_header.encode("utf-8"))
        new_client_socket.send(response_body)
    #  服务完毕，关闭套接字
    new_client_socket.close()


def main():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # socket.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定端口
    server_socket.bind(("",9999))
    # listen监听
    server_socket.listen(128)
    while True:
        # accept 接收分配服务
        new_client_socket, addr = server_socket.accept()
        #提供服务
        service_client(new_client_socket)
    # 关闭套接字
    server_socket.close()


if __name__ == '__main__':
    main()

