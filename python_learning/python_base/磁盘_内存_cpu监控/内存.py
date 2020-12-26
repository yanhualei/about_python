import psutil
import os

info = psutil.virtual_memory()
print(psutil.disk_io_counters())
print(info)

# print(u'内存使用：',psutil.Process(os.getpid()).memory_info().rss)
total_memory = (info.total)//1024//1024
used_memory = (info.used)//1024//1024
free_memory = (total_memory-used_memory)
print(u'总内存：',(total_memory),end="MB\n")
print("已用内存：",used_memory,end="MB\n")
print("空闲内存：",(free_memory),end="MB\n")
print(u'内存占比：',info.percent)
print(u'cpu个数：',psutil.cpu_count())
