class PlayGame(object):
    L = []
    def __init__(self,name,score):
        self.name =name
        self.score = score
    @staticmethod
    def start_game():
        print("游戏开始了，各位加油啊。。。")

    def print_score(self):

        print("%s的得分是：%d"%(self.name,self.score))
        self.L.append(self.score)

    @classmethod
    def game_over(cls):
        max_score= sorted(cls.L, reverse=True)
        print("最高得分：%s"%max_score[0])

# 调用静态方法
PlayGame.start_game()

# 打印小明分数
xiaoming = PlayGame("小明",80)
xiaoming.print_score()

# 打印小花分数
xiaohua = PlayGame("小花",67)
xiaohua.print_score()

# 打印小刚分数
xiaogang = PlayGame("小刚",99)
xiaogang.print_score()

# 调用类方法
PlayGame.game_over()





