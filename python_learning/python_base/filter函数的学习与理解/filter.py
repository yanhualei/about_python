# filter
#个人理解：filter作用类似于reduce，函数作用于序列每一个元素,并根据条件挑选目标元素
#取列表内元素的偶数部分
def is_oushu(n) :
    return n % 2 == 0
ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]
lis = list(filter(is_oushu, ls))
print(lis)

#删除空字符串
def move_empty(s):
    return  s and s.strip()   # strip()去掉空字符,strip('a')去掉'a'
print(list(filter(move_empty, ["a", 'f', None, ' ', ''])))


#利用filter打印自然数中所有的回文数
def is_palindrom(n):  #验证回文数
    n = str(n)
    m = n[::-1]
    return m == n

def do_print():  # 打印回文数
    return filter(is_palindrom,[x for x in range(1,1000)])

print(list(do_print()))

# 打印自然数中所有的素数
# (1)构造一个无限的奇数序列
def is_oddnumber():
    n = 1
    while True:
        n = n+2
        yield n
# (2)定义一个筛选器
def _not_divisible(n):
    return lambda x : x % n > 0
# (3)定义一个生成器，不断返回下一个素数，即质数，只能被1和本身整除
def primes():
    yield 2
    it = is_oddnumber()  # 先初始化数列
    while True:
        n=next(it)
        yield  n
        it = filter(_not_divisible,it)

# 打印想要的素数
for k in primes():
    if k < 100:
        print(k)
    else:
        break
