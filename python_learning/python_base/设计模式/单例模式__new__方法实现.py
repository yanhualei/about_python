
class Singleton(object):
    """
    利用重写__new__方法实现单例模式
    """
    instance = None

    def __new__(cls):
        if cls.instance is None:  # 如果本类没有_instance属性
            cls.instance = super().__new__(cls)
        return cls.instance



single1 = Singleton()
single2 = Singleton()
print(id(Singleton()))  # 类对象
print(id(single1))  # 实例对象1
print(id(single2))  # 实例对象2
print(single1 is single2)