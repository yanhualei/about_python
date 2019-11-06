# 用于格式化输出，当执行print(obj)时，会自动调用


class  Test_str(object):
    def __init__(self):
        self.name = "oldman"

    def __str__(self):  # 用于格式化输出，执行print(obj)时，会自动调用
        return "i am %s"%self.name



test_str = Test_str()
print(test_str)