#sorted:默认是由小到大排序的
#数字排序
print(sorted([1,3,5,64,24,47,79,-5,2,3,5]))
print(sorted([1,3,5,64,24,47,79,-5,2,3,5],key=abs))
#字符串排序
#对于字符串排序，是按照ASCII的大小排序，
#'Z'<'a'，所以大写的Z会放在a的前面
#---------------------------------------->直接比较，默认由小到大
print(sorted(['Bob','about','zoo','Create','Abs'])) # 由每个单词的首字母来比较大小，由此可见，大写字母ASCII都小于小写字母
#---------------------------------------->所有字母转换到小写，然后比较
print(sorted(['Bob','about','zoo','Create','Abs'],key=str.lower))#'about'<'Abs',当所有元素都转换到小写字母时
#当两个单词的首字母相同时，sorted会继续比较下一个单词
##---------------------------------------->由大到小排序
print(sorted(['Bob','about','zoo','Create','Abs'],key=str.lower,reverse=True))

#例题：将下面学生的名字和成绩排序
#按名字排序
L=[('Bob',75),('admin',80),('bart',66),('xiaohong',90),('Lisa',100)]
#读取L中的学生姓名

# def name(t):
# 	return t[0]
# def score(t):
# 	return t[1]

print("按照姓名排序：",sorted(L,key=lambda l:l[0]))
print("按照成绩排序，由大到小：",sorted(L,key=lambda l:l[1],reverse=True))

#解题感悟：重点理解sorted的作用原理，sorted也是作用于序列的每个元素，所以不用循环也可获取序列的每个元素
#所以我们直接定义一个函数，用来获取列表L中的name和score就可以了，然后
#用key关键字获取排序规则，从而规定用什么方式排序


D = [{'name':'oldman','age':18},
	 {'name':'oldman3','age':19},
	 {'name':'oldman2','age':20}]
# 将D中的元素按照age的顺序倒序排列
print(sorted(D,key=lambda d:d["age"] ,reverse=True))
# 将D中的元素按照name的顺序排列
print(sorted(D,key=lambda d:d["name"] ,reverse=False))

# 注：sorted(第一个参数：Iterable，第二个参数：按照哪一列或者说是哪个字段，哪个元素进行排列，
# 第三个参数：按照顺序还是倒序，默认顺序)