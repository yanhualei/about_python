class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

class Student2(object):

    @property  # 装饰score，可以以属性的方式获取score值
    def score(self):
        return self._score

    @score.setter  # student2.score = 100时调用此方法，也就是赋值的时候调用此方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

if __name__ == '__main__':
    student1 = Student()
    student2 = Student2()

    # student的分数设置和获取:设置分数和获取分数得分别需要调用两个方法，并且以方法的形式调用，不够优雅
    # student1.set_score(88)
    # student1.set_score(101)
    # print(student1.get_score())

    # @property 对分数的设置和获取:可以将方法当做属性一样调用，用着舒服看着顺眼，推荐使用
    student2.score = 99
    print(student2.score)