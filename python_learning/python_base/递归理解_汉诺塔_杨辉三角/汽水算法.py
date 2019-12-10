#  一瓶汽水1元钱，两个空瓶能换一瓶汽水，3个瓶盖换一瓶汽水，20元钱能买到多少瓶汽水

def digui(total, bottle_cap=0, empty=0):
    if (total+bottle_cap)<3 and (total+empty)<2:  # 本次的汽水+剩余的瓶盖小于3，并且本次剩余的空瓶+本次的汽水小于2就没办法兑换了
        return total
    bottle_cap = bottle_cap + total
    empty = empty + total

    return total+digui(bottle_cap//3+empty//2,bottle_cap%3,empty%2)
    # digui(bottle_cap // 3 + empty // 2, bottle_cap % 3, empty % 2)  # 下一次能兑换的汽水数量

result = digui(20)
print(result)