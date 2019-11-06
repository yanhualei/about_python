#士兵突击
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
            self.bullet_count -= 1
ak47 = Gun("AK47")
m4a1 = Gun("M4A1")
awm = Gun("AWM")


class Soldier:
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun
    def fire(self):
        if self.gun is None:
            print("%s还没有枪"%self.name)
            return
        else:
            print("%s拿着%s,正在巡逻...\n"%(self.name,self.gun.model))


            print("三分钟后，%s发现敌人..."%self.name)
            self.gun.add_bullet(100)
            print("%s当前子弹数量：%d\n"%(self.gun.model,self.gun.bullet_count))


            print("瞄准敌人，开始射击...")
            self.gun.shoot()
            print("biubiu~~...\n%s剩余子弹数量:%d\n"%(self.gun.model,self.gun.bullet_count))
            print("-"*40)
xusanduo = Soldier("许三多",ak47)
xusanduo.fire()

wubanfu = Soldier("五班副",m4a1)
wubanfu.fire()

shijin = Soldier("史今",awm)
shijin.fire()
