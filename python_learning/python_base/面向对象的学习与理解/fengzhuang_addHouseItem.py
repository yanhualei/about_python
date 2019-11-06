# 本段代码体现了，一个类的参数可以是另一个类的对象，那么此参数可以访问对象的相关属性和方法

class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return ("[%s]占地%.02f"%(self.name,self.area))
bed = HouseItem("席梦思",20)
table = HouseItem("餐桌",10)
yigui = HouseItem("衣柜",20)

print(bed,table,yigui)



class House:
    def __init__(self,area): # 房子类此时只需要一个面积即可
        self.area =area
        self.freearea =area
        self.item_list = []
    def add_item(self,item):
        """当添加进家具时，家具的相关属性随之加入，此时item参数也是家具类的对象，
         那么item的相关属性也随时可用"""
        print("要添加%s"%item)
        if item.area > self.freearea:
            print("%s的占地面积太大，不能添加"%item)
            return  # 家具类中家具的面积大于房子类中房子的面积，直接跳出方法
        else:
            self.item_list.append(item.name) # list不能直接append  item ，因为此时item是对象，只能用item.name
            self.freearea -= item.area
        print("添加的家具：",self.item_list)
        print("房屋剩余的面积：",self.freearea)

my_house = House(50)
my_house.add_item(bed)
my_house.add_item(table)
my_house.add_item(yigui)