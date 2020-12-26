def warp(obj):
    obj.name = 'python'
    return obj


@warp  # 此装饰器用来修改类属性,name
class Bar(object):
    name = 'PHP'
    def __init__(self):
        pass


print(Bar.name)  # => python