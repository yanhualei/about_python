# 单例模式
class Musics(object):
    instance = None  # 类属性只有当类方法调用时，才会发挥作用
    init_flag = False
    """
    使用类名创建对象时，会先调用__new__()方法，为对象分配内存空间
    """
    def __new__(cls, *args, **kwargs):
        if cls.instance is  None:
            cls.instance=super().__new__(cls) # 用于分配空间
        return  cls.instance
    def __init__(self):
        if not self.init_flag:
            print("初始化音乐播放器")
            self.init_flag = True
player = Musics()
print("第一个对象的内存地址：",id(player))

player2 = Musics()
print("第一个对象的内存地址：",id(player2))

"""
    单例模式：就像音乐播放，我们不能每播放一首歌，就打开一次音乐播放器
开辟一个新音源（实际上就一个喇叭）；而是打开一次播放器，播放第一首歌，
然后切换另一首歌的时候，不用重启播放器，使用第一首歌使用的音源
"""

