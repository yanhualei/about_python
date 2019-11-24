
class Singleton(object):
    """
    利用重写__new__方法实现单例模式
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):  # 如果本类没有_instance属性
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


single1 = Singleton()
single2 = Singleton()

print(id(single1))
print(id(single2))
print(single1 is single2)