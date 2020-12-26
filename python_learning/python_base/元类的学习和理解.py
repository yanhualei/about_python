""""""
# 元类：创建类对象的类
"""暂时作为了解内容"""
# 元类的作用： 创建类
# 自定义元类作用：修改类的方法和属性，改变类的创建过程


class test1(object):
    ...
    bar="bar"

test = type("test1",(object,),{"bar":print("我是元类type创建的类")})
print(type(test))
# test.bar

"""
orm:对象关系映射（object relationship mapping）
类名对应表名
类属性对应表列
作用：可以使编程直接面向数据库，面向对象编程
当你操作对象时，orm会帮你做映射，去操作数据库
"""