def output(l):
    print(l[::-1])


if __name__ == '__main__':
    while True:
        strs = input("请输入字符串:\n")

        l = []
        for i in strs:
            l.append(i)
        output(l)