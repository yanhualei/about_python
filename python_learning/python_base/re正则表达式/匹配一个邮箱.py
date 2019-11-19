import re



def main():
    while True:

        # 得到邮箱字符串
        ret = input("请输入邮箱：")
        # 对邮箱字符创进行正则匹配
        # 要求@前要有4-20位
        email = re.match(r"^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$",ret)
        if email:
            print("%s------>符合匹配"%email.string)
        else:
            print("%s------>不符合匹配"%email)
        if email =="exit":
            break


if __name__ == '__main__':
    main()