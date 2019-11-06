class Animal:
    count = 0
    # 实例方法

    def __init__(self,name):
        self.name = name

    def re_name(self):
        self.name = "$" + self.name
        return self.name

    @classmethod  # 只访问类属性
    def run_number(cls):
        cls.count += 1
        print("前面有%d个人在跑步..."%cls.count)

    @staticmethod # 既不需要类属性也不需要实例属性，不需要实例化，直接用类名调用
    def eat():
        print("那只猫好可爱！")

# 调用实例方法

elephant = Animal("大象")
print(elephant.name)
print(elephant.re_name())

#  调用类方法
Animal.run_number()

# 调用静态方法

Animal.eat()
