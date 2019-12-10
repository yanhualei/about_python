# 1元一瓶汽水，2个空瓶换一瓶汽水，3个瓶盖换一瓶汽水，20元能喝多少汽水

def qishui(qs,empty=0,bootle_cap=0):
    """递归实现"""
    if qs+empty<3 and qs+bootle_cap<2:
        return qs
    empty = qs+empty
    bootle_cap = qs +bootle_cap
    return qs+qishui(empty//2+bootle_cap//3,empty%2,bootle_cap%3)

if __name__ == '__main__':
    qs=20
    res = qishui(qs)
    print(res)