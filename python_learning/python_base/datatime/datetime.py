import datetime
#2018-04-01 11:38:54
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "星期："+str(datetime.datetime.now().isoweekday()))