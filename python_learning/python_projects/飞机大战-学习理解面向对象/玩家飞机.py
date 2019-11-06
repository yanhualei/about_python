import pygame
from pygame.locals import *
import random
import sys
import time

# 定义常量(定以后不再更改)注python中没有常量这个概念，
# 为了说明问题，相对于其他语言的常量而言的，其实也就是个全局变量
# 常量每个字母都大写
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

#创建英雄飞机类
class HeroPlane:
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
    def move_left(self):
        #向左飞行
        self.x -= 8
    def move_right(self):
        # 向右飞行
        self.x += 8
def main():
    """定义主函数，一般为程序的入口"""
    pygame.init()

    #创建窗口 set_mode(设置窗口尺寸)display()动态方法，pycharm不提示
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    # 将背景图片加载到内存 load（背景图片的路径）
    bg_img = pygame.image.load("res/img_bg_level_1.jpg")
    # 创建对象
    hero_plane = HeroPlane ("res/hero2.png",240,500,window)

    while True:
        # 将背景图贴到窗口中 blit（图片和窗口的坐标都是：左上角(0,0)）
        window.blit(bg_img,(0,0))
        # 贴飞机图
        hero_plane.display()
        # 贴子弹图
        # 刷新界面，不刷新不会更新现实的内容
        pygame.display.update()
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                sys.exit()# 让程序终止
                pygame.quit()
            # 判断是否按下了键(小面这种按一下，移动一下，用户体验度非常不好，逻辑没错，但是方法不好，不用)
            # elif event.type == KEYDOWN:
            #     if event.key == K_LEFT:
            #         hero_plan.move_left()
            #     elif event.key == K_RIGHT:
            #         hero_plan.move_right()
            # 获取按键连续按下的情况
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            hero_plane.move_left()
        if pressed_keys[pygame.K_RIGHT]:
            hero_plane.move_right()
        time.sleep(0.01)
if __name__ == '__main__':
    main()




