# 什么是猴子补丁(Monkey Patch)？
# 在运行期间动态修改一个类或模块

# 示例1：
class A:
    def func(self):
        print("Hi")
    def monkey(self):
        print("Hi, monkey")
a = A()
A.func=A.monkey   #在运行的时候，才改变了func
a.func()

# 示例2：
class A:
    def func(self):
        print("Hi")
    def monkey(self):
        print("Hi, monkey")

def outer_monkey(a):  # a 这个参数是没有用到的，因为func有一个参数，如果这个函数没有参数的话不能这样直接赋值
    print("Hi,outer monkey")

a = A()
A.func=outer_monkey
a.func()

# 实用场景1：
#假如我们项目中很多代码用到 import json，后来发现ujson性能更高，
# 如果觉得把每个文件的import json 改成 import ujson as json成本较高
# 我们就可以使用下面的方法：猴子补丁
import json
import ujson

def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads

monkey_patch_json()
print(json.__name__)  #

