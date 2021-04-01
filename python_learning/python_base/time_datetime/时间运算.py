import datetime
import time

# 格式化时间方法一
print(datetime.datetime.now())
print(datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d-%A %H:%M:%S"))

# 格式化时间方法二
print(time.localtime())
print(time.strftime("%Y-%m-%d-%A %H:%M:%S",time.localtime()))



# 计算两个日期相差时间
d1 = datetime.datetime.strptime('2012-03-03 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2012-03-02 17:41:19', '%Y-%m-%d %H:%M:%S')
# print(type(d1))
delta = d1 - d2
# print(delta.days)  # 精确到天
print(delta.total_seconds())  # 精确到秒

# 计算三天前的日期
now=datetime.datetime.now()
delta=datetime.timedelta(days=3)
n_days=now-delta
print(n_days.strftime('%Y-%m-%d %H:%M:%S'))
