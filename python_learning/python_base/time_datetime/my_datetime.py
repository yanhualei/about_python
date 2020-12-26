import datetime

# module 'datetime' has no attribute 'now'：报错没有这个属性，原因是文件名和模块名重名
#2018-04-01 11:38:54
a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(a,type(a))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "星期："+str(datetime.datetime.now().isoweekday()))
# **************************************************************
time1 = datetime.datetime.now()
print(type(time1))
my_list = [i for i in range(100000000)]
time2 = datetime.datetime.now()

print(time2-time1)
# **************************************************************
# d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
# d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
# delta = d1 - d2
# print(delta)

