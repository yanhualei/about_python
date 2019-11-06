# 可变参数练习
def variable(*mumbers): # 传入的参数数量，类型不受限制 ，传入的变量在函数内部自动组成一个tuple
	for n in mumbers:
		print(n)

variable(("A",'B','C','D'),['1','2','3'],'hellow')
#关键字参数

def person2(name,age,**le):  # 传入的参数数量，类型不受限制，传入的变量在函数内部自动组成一个dict
	print ('name:',name,'age:',age,'other:',le)
person2(name='xiaohong',age='10',job='computer')

# 命名关键字参数练习
def person(name,age,*,city,job):
	print ('name:',name,'age:',age,'city:',city,'job',job)
person('A','23',city='dalian',job='1991')#命名关键字调用时，须将参数带上

#混合参数练习
def f1(a,c=1,*args,**kw):  # 混合参数顺序不可变必选参数，默认参数，可变参数，命名关键字参数，关键字参数
	print("a=",a,'c=',c,'args=',args,'kw=',kw)
f1(a=3,d=7)
f1(44,3,'xiaoming',x=100)
f1(a=11,c=0.1,v='nihao',y=1000,z='banana')

def f2(a,b=0,*,d,**kw):  # 默认参数的数值调用时可更改，也可缺省
	print('a=',a,'b=',b,'d=',d,'kw=',kw)
f2(a=1,b=2,d=3,f=4)
f2(a=3,d=0,kw=None)  # 当关键字参数没有参数传入时，用None代替，不可省略，特定情况下会出错














