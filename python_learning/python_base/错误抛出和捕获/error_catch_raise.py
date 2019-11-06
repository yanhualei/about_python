# 捕获错误
def error():
    try:
        num = int(input("请输入数字："))
        tol = 10/num
    except ValueError as e:
        return "类型错误:输入的内容不是一个数字"
    except ZeroDivisionError as e:
        return "除零错误，请输入非零数字"
    except  Exception as e:
        return "未知错误："
    else:
        return  tol

if __name__ == '__main__':
    print(error())



# 因业务需求，主动主动抛出错误并且捕获
# 要求密码长度不得少于8位
# 要求密码由数字和字母组成，纯数字或者纯字母都要抛出错误

#
# def pwd():
#     user_pwd = input("请输入密码：") # 此处不能用int()函数转换，因为int类型不是序列，没有长度
#     if len(user_pwd) >8:
#         if not user_pwd.isdigit():
#            # if not user_pwd.isalpha():  # 此处输入汉字也可运行,python内部表示字符串用unicode
#                 # 而unicode中，按照LETTER的方式编码，汉字的前半部也是字母，所以汉字也属于alpha
#             if not user_pwd.encode("UTF-8").isalpha():
#                 return user_pwd
#             else:
#                 allword_ex = Exception("不能是纯字母")
#                 raise allword_ex
#         else:
#             allnum_ex = Exception("不能是纯数字")
#             raise allnum_ex
#     else:
#        ex = Exception("密码长度不得少于8位！")
#        raise ex
#
# try:
#    password =pwd()
#    print(password)
# except Exception as e:
#     print("发现错误：",e)