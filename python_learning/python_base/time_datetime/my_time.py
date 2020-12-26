import time
import datetime
print("ctime:",time.ctime())
print("time:",time.time())  # time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
print("localtime:",time.localtime().tm_hour)

print(datetime)