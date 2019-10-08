import pygame
from pygame.locals import *
from sys import exit
import time
import threading
import numpy

enemy_list = []
hero_list = []
EXIT_NUM = 0
blood_Lock = threading.Lock()
enemy_lock = threading.Lock()

#地图的道路与草坪
background_arraylist = [
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1]
]

background_flowers_filename = "images/flowers.png"
background_road_filename = "images/sky.png"
enemy_image_filename = "images/enemy.png"
hero_image_filename = "images/hero.png"
shell_image_filename = "images/shell.png"
blood_image_filename = "images/blood.png"


pygame.init()

screen = pygame.display.set_mode((960,700),0,32)
pygame.display.set_caption("塔防游戏")

background_flowers = pygame.image.load(background_flowers_filename).convert()
background_road = pygame.image.load(background_road_filename).convert()
enemy_image = pygame.image.load(enemy_image_filename).convert_alpha()
hero_image = pygame.image.load(hero_image_filename).convert_alpha()
shell_image = pygame.image.load(shell_image_filename).convert_alpha()
blood_image = pygame.image.load(blood_image_filename).convert_alpha()

#炮弹类
class shell:
    shell_speed = 0
    shell_image = None
    shell_position= [0,0]
    shell_sin = 0
    shell_cos = 0
    shell_ATK = 10
    #设置炮弹飞行方向
    def move(self):
        self.shell_position = [self.shell_position[0] + (self.shell_cos * self.shell_speed),self.shell_position[1] + int(self.shell_sin * self.shell_speed)]
    #判断是否与敌人相碰撞
    def is_crash(self,enemy):
        x= self.shell_position[0] - enemy.enemy_position[0]
        y = self.shell_position[1] - enemy.enemy_position[1]
        if -21 <= x <= 50 and -21 <= y <=50:
            return True
        return False
#敌军类
class enemy:
    enemy_speed = 0
    enemy_position = [200,0]
    enemy_image = None
    Previous_path = [-1,0]
    curDirection = [0,0]
    blood_position = [0,0]
    blood = 0
    blood_image = None

    #移动函数
    def move(self):
        self.find_road()
        self.enemy_position = [self.enemy_position[0] + self.curDirection[0] * self.enemy_speed,self.enemy_position[1] + self.curDirection[1] * self.enemy_speed]
        print(self.blood // 2)
        self.blood_position = [self.enemy_position[0] + (50 - self.blood) // 2,self.enemy_position[1] + 40]
        if self.enemy_position[0] >1000 or self.enemy_position[1] > 800:
            enemy_list.remove(self)
    #判断下一步向什么地方走，使用迷宫方式来寻找,使用列表内嵌套元组方式，remove方法去掉上次的位置，来搜索剩余三个方向。
    def find_road(self):
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        direction.remove(self.Previous_path)
        for dic in direction:
            try:
                if background_arraylist[int(self.enemy_position[1]// 50+ dic[1])][int(self.enemy_position[0] // 50 + dic[0])] == 0:
                    self.curDirection = dic
                    self.Previous_path = [-dic[0],-dic[1]]
                    break
            except IndexError:
                pass
    #被攻击后掉血
    def be_attack(self,ATK):
        blood_Lock.acquire()
        if self.blood >= ATK:
            self.blood -= ATK
        else:
            self.blood = 0
        blood_Lock.release()
        print(self.blood)

#炮塔类
class hero:
    shell_list = [0]
    #攻击范围
    area = 0
    hero_style = None
    hero_position = [0,0]
    #攻击
    def attack(self,produce_shell):
        if len(self.shell_list) != 0:
            if self.shell_list[0] == 0:
                self.shell_list = self.shell_list[0] + 1
                self.shell_list = []
        self.shell_list.append(produce_shell)
    #判断敌军是否在攻击范围内
    def judge_isInArea(self,enemy):
        distance_x = enemy.enemy_position[0] -self.hero_position[0]
        distance_y = enemy.enemy_position[1] - self.hero_position[1]
        distance =numpy.sqrt(numpy.square(distance_x) + numpy.square(distance_y))
        if distance <= self.area:
            produce_shell = shell()
            produce_shell.shell_sin = distance_y / distance
            produce_shell.shell_cos = distance_x / distance
            produce_shell.shell_position = [self.hero_position[0] + 25,self.hero_position[1] + 25]
            produce_shell.shell_image = shell_image
            produce_shell.shell_speed = 20
            return produce_shell
        return None

#生产敌军
def produce_army():
    for p in range(10):
        produce_enemy = enemy()
        produce_enemy.blood_image = blood_image
        produce_enemy.blood = 100
        produce_enemy.enemy_speed = 3
        produce_enemy.enemy_image = enemy_image
        enemy_lock.acquire()
        enemy_list.append(produce_enemy)
        enemy_lock.release()
        time.sleep(1)
    time.sleep(4)
    for k in range(5):
        produce_enemy = enemy()
        produce_enemy.blood_image = blood_image
        produce_enemy.blood = 100
        produce_enemy.enemy_speed = 6
        produce_enemy.enemy_image = enemy_image
        enemy_lock.acquire()
        enemy_list.append(produce_enemy)
        enemy_lock.release()
        time.sleep(1.5)

#炮塔的自我检测：
def hero_judge(hero):
    global EXIT_NUM
    while True:
        if EXIT_NUM == 1:
            break
        for enemy in enemy_list:
            shell = hero.judge_isInArea(enemy)
            if shell != None:
                hero.attack(shell)
                time.sleep(0.5)
                break
        time.sleep(0.02)

#检测被选中的地方是否已经有hero了
def is_exist(position):
    for hero in hero_list:
        if hero.hero_position == position:
            return True
    return False
#刷新界面的图片
def interface_update():
    #背景图片加载
    x_position = 0
    y_position = 0
    for y in background_arraylist:
        for x in y:
            if x == 1:
                screen.blit(background_flowers,(int(x_position * 50),int(y_position * 50)))
            else:
                screen.blit(background_road,(int(x_position * 50),int(y_position * 50)))
            x_position+=1
        x_position = 0
        y_position +=1
    #加载炮塔
    for hero in hero_list:
        screen.blit(hero.hero_style,hero.hero_position)
        if len(hero.shell_list) != 0:
            if hero.shell_list[0] !=0:
                for shell in hero.shell_list:
                    shell.move()
                    screen.blit(shell.shell_image,shell.shell_position)
                    for enemy in enemy_list:
                        if shell.is_crash(enemy):
                            enemy.be_attack(shell.shell_ATK)
                            hero.shell_list.remove(shell)
                            break
    #加载敌军
    for enemy in enemy_list:
        if enemy.blood == 0:
            enemy_list.remove(enemy)
            break
        enemy.move()
        for x in range(enemy.blood // 2):
            enemy.blood_position = [enemy.blood_position[0] +2,enemy.blood_position[1]]
            screen.blit(enemy.blood_image,enemy.blood_position)
        screen.blit(enemy.enemy_image,enemy.enemy_position)

#监听各种事件并作出反应
def keepOn_eye():
    global EXIT_NUM
    for event in pygame.event.get():
        #12是关闭窗口的代码
        # print(event.type)
        if event.type == pygame.QUIT:
            EXIT_NUM = 1
            pygame.quit()
            exit()
        if event.type == 5:
            x,y = pygame.mouse.get_pos()
            if background_arraylist[y // 50][x // 50] == 1:
                produce_hero = hero()
                produce_hero.hero_style = hero_image
                produce_hero.area = 150
                position = [(x // 50) * 50,(y // 50) * 50]
                if not is_exist(position) :
                    produce_hero.hero_position = position
                    hero_list.append(produce_hero)
                    threading.Thread(target=hero_judge,args=(produce_hero,)).start()

def main():
    threading.Thread(target=produce_army).start()
    global EXIT_NUM
    while True:
        if EXIT_NUM == 1:
            break
        #事件监听
        keepOn_eye()

        #各种内容加载
        interface_update()

        time.sleep(0.02)


        pygame.display.update()

if __name__ == '__main__':
    main()