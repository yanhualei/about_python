import pygame
from pygame.locals import *
import random
import sys
import time

# 定义常量(定以后不再更改)注python中没有常量这个概念，
# 为了说明问题，相对于其他语言的常量而言的，其实也就是个全局变量
# 常量每个字母都大写
WINDOW_HEIGHT = 768 # 窗口宽高
WINDOW_WIDTH = 512

ENEMY_COUNT = random.randint(1,6)  # 敌机数量
ENEMY_SPEED = 5 # 敌机速度
enemy_plane_list = []  # 敌机列表

BULLET_SPEED = 5  # 子弹速度

score = 0  # 记录得分

class BasePlane: # 基础飞机类
    def __init__(self,img_path,x,y,window):
        # 飞机图片
        self.img =pygame.image.load(img_path)
        # 飞机坐标
        self.x = x
        self.y = y
        # 飞机所在窗口
        self.window = window
    def display(self):
        """贴飞机图"""
        self.window.blit(self.img,(self.x,self.y))
class HeroPlane(BasePlane):   #继承基础飞机类
    def __init__(self,img_path, x, y, window):
        super().__init__(img_path, x, y, window )  # 继承父类属性
        self.bullets = []
    def move_left(self):
        #向左飞行
        self.x -= 8
    def move_right(self):
        # 向右飞行
        self.x += 8
    def fire(self):
        """发射子弹"""
        bullet = HeroBullet("res/bullet_9.png", self.x+50,self.y-31,self.window)
        # 要显示多个子弹，需要将子弹存储起来，然后同时贴在最新的页面，否则整个游戏窗口只能看见一个子弹
        self.bullets.append(bullet)
    def display_bullet(self):
        """贴子弹图"""
        # 定义一个空列表来回收飞出窗口的子弹图片
        out_bullets = []
        for bullet in self.bullets:
            if bullet.y > -31:  # 如果子弹还在窗口内
                for enemy in enemy_plane_list:  # 遍历所有敌机
                    if bullet.is_hit_plane(enemy):  # 判断子弹是否和敌机相撞
                        out_bullets.append(bullet)   #  将击中敌机的子弹存到列表
                        enemy.is_hited = True  # 修改被击中敌机的状态
                        global score
                        score += 10
                        break
                    bullet.display()  # 贴子弹图片
                    bullet.move()  # 让子弹飞
            else:  # 如果子弹飞出边界
                # 注意：不要直接在列表中删除元素，否则会导致错误
                out_bullets.append(bullet)
        for out_bullet in out_bullets:
            self.bullets.remove(out_bullet)

    def is_hit_enemy(self, enemy):
        if pygame.Rect.colliderect(
            pygame.Rect(self.x, self.y, 120, 78),
            pygame.Rect(enemy.x, enemy.y, 100, 68)
        ):  # 判断是否交叉
            return True
        else:
            return False
    def display(self):
        """贴图"""
        for enemy in enemy_plane_list:
            if self.is_hit_enemy(enemy):
                enemy.is_hited = True
                time.sleep(5)
                sys.exit()
                break

        self.window.blit(self.img, (self.x, self.y))

class HeroBullet:
    """子弹类"""
    def __init__(self,path_img,x,y,window):
        """

        :param path_img: 子弹图片路径
        :param x: 子弹x坐标
        :param y: 子弹的y坐标
        :param window: 窗口对象
        """
        # 注意：实例化子弹对象时，传进来的图片参数要从磁盘加载到内存，才能直接使用
        self.bullet_img = pygame.image.load(path_img)
        self.x = x
        self.y = y
        self.window = window
    def display(self):
        """贴子弹图片"""
        self.window.blit(self.bullet_img,(self.x,self.y))
    def move(self):
        """子弹移动"""
        self.y -= BULLET_SPEED
    def is_hit_plane(self,enemy):
        # 获取图片对象
        bullet_rec = Rect(self.x,self.y,20,31)
        enemy_rec = Rect(enemy.x,enemy.y,100,68)
        # 判断两个矩形是否相交，相交返回True，否则返回False
        return pygame.Rect.colliderect(bullet_rec,enemy_rec)

class EnemyPlane(BasePlane):  # 继承基础飞机类
    """敌机类"""
    def __init__(self,path_img,x,y,window):
        # 继承父类属性
        super().__init__(path_img,x,y,window)
        self.is_hited = False
    def move(self):
        """敌机移动"""
        self.y += ENEMY_SPEED
        # 处理敌机飞出窗口边界的情况，当敌机飞出窗口下边界，重置y值，让飞机飞到顶部
        if self.y >= WINDOW_HEIGHT or self.is_hited:
            self.x = random.randint(0,512-100)  # 让敌机在窗口顶部随机出现，窗口宽度512，敌机宽度100
            self.y = random.randint(-300,-100)  # 为了让敌机不同时出现，出现一排的现象
            self.enemy_img = pygame.image.load("res/img-plane_%d.png"%random.randint(1,7))
            if self.is_hited:
                # 把属性值修改回来
                self.is_hited = False

class Map:
    """地图类"""
    def __init__(self, path_img, x, y, window):
        """
        对象初始化
        :param path_img: 地图图片路径
        :param x: 地图x坐标值
        :param y: 地图y坐标值
        :param window: 窗口对象
        """
        self.img = pygame.image.load(path_img)
        self.x = x
        self.y = y
        self.window = window
        self.img2 = pygame.image.load(path_img)
        self.img2_y = -WINDOW_HEIGHT

    def display(self):
        """贴地图图片"""
        self.window.blit(self.img, (self.x, self.y))
    def move(self):

        # 当地图1的y值移动出窗口，则重置位置
        if self.y >= WINDOW_HEIGHT:
            self.y = -WINDOW_HEIGHT
        # 当地图2的y值移动出窗口，则重置位置
        if self.img2_y >= WINDOW_HEIGHT:
            self.img2_y = -WINDOW_HEIGHT
        # 两张地图都移动，每次移动3个像素
        self.y += 3
        self.img2_y += 3

        self.window.blit(self.img2, (self.x, self.img2_y))

def main():
    """定义主函数，一般为程序的入口"""
    pygame.init()  # 创建pygame库，导入所有的模块

    #创建窗口 set_mode(设置窗口尺寸)display()动态方法，pycharm不提示
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    # 将背景图片加载到内存 load（背景图片的路径）
    map = Map("res/img_bg_level_%d.jpg" % random.randint(1, 5), 0, 0, window)
    # 创建英雄飞机对象
    hero_plane = HeroPlane ("res/hero2.png",240,500,window)
    # 创建多架敌机对象
    for _ in range(ENEMY_COUNT):
        enemy_plane = EnemyPlane("res/img-plane_%d.png"%random.randint(1,7), random.randint(0, 500 - 100), -70, window)
        enemy_plane_list.append(enemy_plane)
    #  加载自定义字体，返回字体对象
    font_obj = pygame.font.Font("res/SIMHEI.TTF", 35)
    while True:
        # 将背景图贴到窗口中 blit（图片和窗口的坐标都是：左上角(0,0)）
        map.display()
        # 地图移动
        map.move()
        # 贴子弹图
        hero_plane.display_bullet()
        # 贴敌机图
        for enemy_plane in enemy_plane_list:
            enemy_plane.display()
            enemy_plane.move()
        # 贴飞机图
        hero_plane.display()
        # 贴字体图
        # 设置文本，返回文本对象   render(文本内容， 抗锯齿，颜色)
        text_obj = font_obj.render("得分 %s" % score, 1, (178, 255, 255))
        window.blit(text_obj, (10, 10))
        # 刷新界面，不刷新不会更新现实的内容
        pygame.display.update()
        # 获取键盘事件
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                sys.exit()# 让程序终止

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                     hero_plane.fire()
            # 判断是否按下了键(小面这种按一下，移动一下，用户体验度非常不好，逻辑没错，但是方法不好，不用)
            # elif event.type == KEYDOWN:
            #     if event.key == K_LEFT:
            #         hero_plan.move_left()
            #     elif event.key == K_RIGHT:
            #         hero_plan.move_right()
            # 获取按键长按下的情况
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_SPACE]:
        #     hero_plane.fire()

        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            if hero_plane.x != 0:
                hero_plane.move_left()
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            if hero_plane.x <= WINDOW_WIDTH - 120:
                hero_plane.move_right()
        time.sleep(0.005)


if __name__ == '__main__':
    main()






