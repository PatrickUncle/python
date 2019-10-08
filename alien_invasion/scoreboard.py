import pygame.font as font
from ship import Ship
from pygame.sprite import Group
class ScoreBoard():
    """显示得分信息的类"""

    def __init__(self,ai_settings,screen,states):
        """初始化显示得分设计的属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.states = states

        #显示得分信息时用到的字体设置
        self.text_color = (30,30,30)
        self.font = font.SysFont(None,48)


        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.states.score,-1)) # 四舍五入
        score_str = "score:" + "{:,}".format(rounded_score)  #将数字变成千位分隔符格式，好看一些
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #将得分显示在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def prep_high_score(self):

        high_score = int(round(self.states.high_score,-1))
        high_score_str = "highest:" + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        #将最高分放在最高
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render("level:" + str(self.states.level),True,self.text_color,self.ai_settings)

        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.states.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示分数"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)