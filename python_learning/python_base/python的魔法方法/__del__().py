# 这可以说是一个析构器，或者回收器，在对象引用数降到0时执行，有时可能还需要等一会再执行，
# 所以一般不推荐使用，但是在代码中我们偶尔可以用它来实现一些必须要做的，但是并不紧急的事
import sys
import time


class Animal:
    def __init__(self,name):  # 初始化方法，创建完对象后会直接调用
        self.__name = name

    def __del__(self):# 析构方法,当对象被删除时，会自动被调用
        print("__del__方法被调用")
        print("%s对象已经被干掉了..." % self.__name)


dog = Animal('oldman')

del dog  # 手动删除对象时，如果此对象没有了其他引用，__del__会被调用

cat = Animal('white')
cat2 = cat
cat3 = cat

print(sys.getrefcount(cat))  # 打印cat引用计数
print("---马上 删除cat对象")
del cat  # 结果显示，删除cat对象时，不会调用del方法，因为white还有其他引用
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3  # 删除cat3对象时，会调用del方法，因为white没有有其他引用

print("程序2秒钟后结束")
time.sleep(2)