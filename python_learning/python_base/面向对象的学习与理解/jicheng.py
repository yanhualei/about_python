# 继承
class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


wangcai = Dog()
mimi = Cat()

wangcai.run()  # 狗类完全继承动物类的run()方法
mimi.run()  # 猫类完全继承动物类的run()方法
# 所以结果出现Animal is running...
# 这就是继承(继承分为类继承，方法继承，属性继承)，但是方法继承和属性继承都是在类继承的基础之上才会出现