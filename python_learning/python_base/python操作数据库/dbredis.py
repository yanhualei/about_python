from redis import Redis

redis_conn = Redis(host='127.0.0.1', port=6379)
add_data = redis_conn.sadd("test","werqwrqewrq")  # 添加成功返回1，添加失败返回0
print(add_data)