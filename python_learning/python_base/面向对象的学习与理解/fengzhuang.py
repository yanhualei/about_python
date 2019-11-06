# 封装
# (1)属性的封装
# class Human:
#     def __init__(self,human_name):
#         self.name = human_name
#     def man(self):
#         print("%s is man!"%self.name)
#     def woman(self):
#         print("%s is woman!"%self.name)
# xiaoming = Human("小明")  # 此时创建对象，会自动调用__init__方法，那么self.name="小明"
# xiaoming.man()
# xiaohong = Human("小红") # 此时创建对象，会自动调用__init__方法，那么self.name="小红"
# xiaohong .woman()

# (2)方法的封装
class Person:
    def __init__(self,name,weight):  # 初始化类属性，每个对象的属性互不影响
        self.name = name
        self.weight = weight
    def __str__(self):  # 必须有返回值，当需要返回对象变量值时，可以使用此方法
        return ("我是%s,我的体重是%d"%(self.name,self.weight))
    def run(self): # 共享对象的所有属性，故不需要写入参数
        self.weight = self.weight - 2
        print("我是%s，跑步后的体重是%d"%(self.name,self.weight))
    def eat(self):  #共享对象的所有属性，不需要写入参数
        self.weight = self.weight + 2
        print("我是%s,吃东西后体重为%d"%(self.name,self.weight))

xiaoming = Person("小明",75)  # 对象实例化，创造一个体重为75的小明对象
print(xiaoming)  # 打印小明这个对象的相关属性信息，因为有__str__方法，所以返回的不是对象的内存地址
xiaoming.run()  # 小明对象调用run()方法
xiaoming.eat()  #小明对象调用eat()方法