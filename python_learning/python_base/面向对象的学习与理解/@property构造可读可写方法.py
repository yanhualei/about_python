class Student:
    def __init__(self, value=0):
        self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score 必须是int类型')
        if value < 0 or value > 100:
            raise ValueError("score 取值范围1-100")
        self._score = value


if __name__ == '__main__':
    # 创建学生
    xiaoming = Student()
    print(xiaoming.score)
    # 设置正确成绩
    xiaoming.score = 100
    print(xiaoming.score)
    # 设置超出范围的成绩
    xiaoming.score = 101
    print(xiaoming.score)
    # 设置非整型的成绩
    xiaoming.score = 'hellow'
    print(xiaoming.score)
