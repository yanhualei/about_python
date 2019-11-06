import pygame
from pygame.locals import *
import sys
import random
import time

WIDTH = 512
HEIGHT = 768
enemy_plane_list = []
class Hero_Plane:
    def __init__(self,img_path,x,y,window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
        self.bullets = []
    def display(self):
        self.window.blit(self.img,(self.x,self.y))  # 注意：blit（）函数第一个参数，图片路径，第二个参数是所在位置，即坐标
    def fire(self):
        bullet = Bullet("res/bullet_9.png",self.x+50,self.y-56,self.window )
        self.bullets.append(bullet)
    def display_bullet(self):
        for bullet in self.bullets:
            bullet.display()
            bullet.move()
    def  move_left(self):
        self.x -= 8
    def move_right(self):
        self.x += 8
    def move_up(self):
        self.y -= 8
    def move_down(self):
        self.y += 8
class Bullet:
    def __init__(self,img_path,x,y,window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
    def display(self):
        self.window.blit(self.img,(self.x,self.y))
    def move(self):
        self.y -= 8
class Enemy_Plane:
    def __init__(self,img_path,x,y,window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
        enrmy_plane_list = []
    def display(self):
        self.window.blit(self.img,(self.x,self.y))
    def is_hited(self):
        pass
    def move(self):
        if self.y < HEIGHT:
            self.y += 5
        else:
            self.y = random.randint(-300,-68)
            self.x = random.randint(0, WIDTH-100)
            self.enemy_img = pygame.image.load("res/img-plane_%d.png" % random.randint(1, 7))
class map:
    pass
def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))  # 创建游戏窗口对象
    bg_img = pygame.image.load("res/img_bg_level_1.jpg")  # 加载背景图片
    hero_plane = Hero_Plane("res/hero2.png", 240, 500, window) # 创建英雄飞机对象
    for _ in range(random.randint(1, 5)):  # 创建1-5内任意个敌机对象
        enemy_plane = Enemy_Plane("res/img-plane_%d.png" % random.randint(1, 7), random.randint(0, WIDTH - 100),
        random.randint(-400, -68), window)
        enemy_plane_list.append(enemy_plane)
    while True:
        window.blit(bg_img, (0,0))  # 在游戏窗口贴背景图
        hero_plane.display()  # 贴英雄飞机
        hero_plane.display_bullet() # 贴飞机子弹
        for enemy_plane in enemy_plane_list:
            enemy_plane.display()   # 贴敌方飞机
            enemy_plane.move()  # 让敌方飞机移动
        pygame.display.update()  # 刷新，不刷新没有效果

        # 检测键盘事件
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    hero_plane.fire()
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_a] or pressed_key[K_LEFT]:
            if hero_plane.x > 0:
                hero_plane.move_left()
        elif pressed_key[K_d] or pressed_key[K_RIGHT]:
            if hero_plane.x < WIDTH-120:
                hero_plane.move_right()
        elif pressed_key[K_w] or pressed_key[K_UP]:
            if hero_plane.y > 0:
                hero_plane.move_up()
        elif pressed_key [K_s] or pressed_key[K_DOWN]:
            if hero_plane.y <HEIGHT-78:
                hero_plane.move_down()



        time.sleep(0.005)

if __name__ == '__main__':
    main()



