class MyCls(object):

    def __init__(self):
        self.__weight = 60

    @property  # my.weight = 100 这是不允许的，my.weight只能get不能set
    def weight(self):
        return self.__weight


my = MyCls()
# my.weight = 100
print(my.weight)