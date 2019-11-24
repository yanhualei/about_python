class MyCls(object):
    __weight=60
    @property
    def weight(self):
        return self.__weight


my = MyCls()
print(my.weight)