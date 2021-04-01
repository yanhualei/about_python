import pika
credentials = pika.PlainCredentials('admin','admin2017')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='127.0.0.1', port=5674,credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='test')


def my_callback(ch, method, properties, body):
    '''回调函数,处理从rabbitmq中取出的消息'''
    print(" [x] Received %r" % body)


channel.basic_consume('test',my_callback,auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()    #开始监听 接受消息