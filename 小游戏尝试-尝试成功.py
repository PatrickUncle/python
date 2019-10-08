import pygame
from pygame.locals import *
from  sys import exit
import time

#定义图片名字
background_image_filename = "images/sushiplate.jpg"
mouse_image_filename = "images/fugu.png"
#进行pygame初始化
pygame.init()

#产生一个窗口，大小分辨率是640*480 第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；32数值为色深。
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Hello,World!")

#获取图片对象
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#游戏数据刷新
while True:
    # #监听全部事件，得到一个事件列表
    for event in pygame.event.get():
        print(event)
        #12是关闭窗口的代码
        if event.type == 12:
            exit()
    #screen对象是整个屏幕的Surface对象，拿来操作屏幕中的东西
    screen.blit(background,(0,0))
    #获取鼠标坐标
    x,y = pygame.mouse.get_pos()

    #设置鼠标控制的图片位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    #使用Surface对象显示出鼠标控制的图片
    screen.blit(mouse_cursor,(x,y))
    #稍微让CPU休息一下，否则会卡住
    time.sleep(0.02)
    #一定要调用的刷新函数，否则屏幕内一片漆黑
    pygame.display.update()
