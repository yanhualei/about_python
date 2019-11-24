def output(l):
    str1=l[::-1]
    print("".join(str1))


if __name__ == '__main__':

    strs = "123456"

    l = []
    for i in strs:
        l.append(i)
    output(l)