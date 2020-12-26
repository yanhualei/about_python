class animal(object):
    def __init__(self):
        pass

dog = animal()  # 创建一个实例：狗狗
cat = animal()  # 创建一个实例：猫咪

print(id(dog))
print(id(cat))
print(dog is cat)

# 我们发现：每次创建一个实例，都会开辟一个新的内存单元，也就是说，每个实例都是新创建的，明显区别于单例模式
