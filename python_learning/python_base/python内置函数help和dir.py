import copy
# Help()函数是一个内置函数，用于查看函数或模块用途的详细说明：
help(copy.copy)

# dir():python内置的函数，
# 1.不带参数时：返回当前范围内的变量、方法和定义的类型列表
# 2.带参数时：返回参数的方法、属性的列表
print(dir())
print(dir(copy.copy))
