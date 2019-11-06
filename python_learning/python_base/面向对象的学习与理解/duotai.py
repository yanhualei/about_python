# 多态：如果看这段代码还不是很理解，建议先去看看继承代码，再来理解多态代码，保证一看就明白了
class Animal(object):
    def run(self):
        print("Animal is running...")

class  Dog(Animal):
    def run(self):
        print("Dog is running...")
class Cat(Animal):
    def run(self):
        print("Cat is running...")
wangcai = Dog()
mimi =  Cat()

wangcai.run()
"""狗类继承了动物类，所以狗类同时拥有动物类的方法，
那么，wangcai.run()表面上是直接调用了自己的方法，
实际上是先调用animal中的run方法然后再调用自己的run()方法。
但是由于狗类重新定义了方法，也就是重写了父类给的方法，可以理解为放弃了父类中自己不喜欢的方法，
然后呈现出自己为自己设计的形态--->“Dog is running...”.那么这种方式在面向对象中就叫做多态
"""

mimi.run()
"""
猫类同狗类，都是利用继承的基础，重写的能力，从而呈现自己形态---->
猫类和狗类利用继承和重写的能力改变了父类所给的方法和属性，从而让自己变得不同
他们的共同作用表现出了多态

"""
#
