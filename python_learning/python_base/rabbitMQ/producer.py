import pika


# producers：生产者

credentials = pika.PlainCredentials('admin','admin2017')  # 创建登录对象
connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='127.0.0.1', port=5674,credentials=credentials))     #定义连接池
channel = connection.channel()  # 创建信道
channel.queue_declare(queue='test')    #声明队列以向其发送消息消息
for i in range(10):
    channel.basic_publish(exchange='', routing_key='test',
                        body='"produceID":"787767667123","price":"%s"'%i)  #注意当未定义exchange时，routing_key需和queue的值保持一致
    print('send success msg to rabbitmq %s'%i)
connection.close()   #关闭连接