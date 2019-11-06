# 有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到第三个
# 月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 1>1  # 单位：对
# 2>1
# 3>2
# 4>3
# 5>5
# 6>8
# 7>13
# 8>21
# .
# .
# 根据规律发现，生兔子问题是一个斐波那契数列问题

def Fibonacci_Yield_tool(n):
    """斐波那契yield写法"""
    a,b = 0,1
    while n > 0:
        a,b = b,a+b
        yield b
        n -=1

if __name__ == '__main__':
    print(list(Fibonacci_Yield_tool(8)))








