class Singleton(type): # type: 元类
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class TypeSingleton(metaclass=Singleton):
    """
    利用元类创建单例模式
    """
    pass
single1 = TypeSingleton()
single2 = TypeSingleton()

print(id(single1))
print(id(single2))
print(single1 is single2)