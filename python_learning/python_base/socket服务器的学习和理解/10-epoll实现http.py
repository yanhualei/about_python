import socket
import re
import select


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求 ，即http请求  
    # GET / HTTP/1.1
    # .....
    # request = new_socket.recv(1024).decode("utf-8")
    # print(">>>"*50)
    # print(request)

    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据，给浏览器
    
    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    #  epoll()表示的是共享内存
    # 创建一个epoll对象，epl表示的是指向了共享内存
    epl = select.epoll()

    # tcp_server_socket.fileno()是监听套接字的文件表示符，是用来映射应用程序的监听套接字
    # select.EPOLLIN是用来监测公共内存中是否有输入，如果有输入，表示有客户端向客户端发起连接
    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:
        # 默认会堵塞，直到 os监测到数据到来 通过事件通知方式 告诉这个程序，此时才会解堵塞
        # epl.poll()返回结果是个列表：
        #  [(fd, event), (套接字对应的文件描述符, 这个文件描述符到底是什么事件 例如 可以调用recv接收等)]
        fd_event_list = epl.poll()
        for fd, event in fd_event_list:
            # 等待新客户端的链接
            # fd是os监测到的套接字文件描述符，也是fd_event_list列表中的第一个元组中的元素，
            # 而第一个元组永远表示的是监听套接字对应的文件标识符和事件，因为epl(共享内存)对象在列表创建之前已经将监听套接字注册内存中
            # tcp_server_socket.fileno()是监听套接字的文件描述符
            if fd == tcp_server_socket.fileno():  # 判断是否是监听套接字
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:  # 判断客户端是否成功连接服务器(判断是否有新的套接字标识符写入到共享内存中)
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")  # 客户端连接服务器成功，服务器开始接收数据请求
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]


    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

