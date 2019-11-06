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

def main():
    """定义主函数，一般为程序的入口"""
    pygame.init()

    #创建窗口 set_mode(设置窗口尺寸)display()动态方法，pycharm不提示
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    # 将背景图片加载到内存 load（背景图片的路径）
    bg_img = pygame.image.load("res/img_bg_level_1.jpg")

    while True:
        # 将背景图贴到窗口中 blit（图片和窗口的坐标都是：左上角(0,0)）
        window.blit(bg_img,(0,0))
        # 贴飞机图
        # 贴子弹图
        # 刷新界面，不刷新不会更新现实的内容
        pygame.display.update()
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                sys.exit()# 让程序终止
                pygame.quit()
        time.sleep(0.02)
if __name__ == '__main__':
    main()




