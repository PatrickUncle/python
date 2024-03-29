import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """飞船类"""

    def __init__(self,ai_settings,screen):
        """初始化飞船  并设置其初始位置"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.rect_x = float(self.rect.centerx)
        self.rect_y = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""

        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect_y += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.rect_x
        self.rect.bottom = self.rect_y

    def center_ship(self):
        """让飞船在屏幕上回归原位"""
        self.rect_x = self.screen_rect.centerx
        self.rect_y = self.screen_rect.bottom