import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_states import GameStates
from button import Button
from scoreboard import ScoreBoard
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一个play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储所有子弹的编组
    bullets = Group()

    # 创建一个用于存储所有外星人的编组
    aliens = Group()

    # 创建一个游戏时统计信息对象
    states = GameStates(ai_settings)

    # 创建一堆外星人
    gf.create_fleet(ai_settings, screen, aliens,ship)

    #创建一个分数板对象
    score = ScoreBoard(ai_settings,screen,states)

    while True:
        #事件监听
        gf.check_events(ai_settings,screen,ship,states,aliens,bullets,play_button,score)
        if states.game_active :
            ship.update()
            gf.update_bullets(ai_settings,screen,bullets,aliens,ship,states,score)
            gf.update_aliens(ai_settings,states,screen,aliens,ship,bullets,score)
        #屏幕更新
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,states,play_button,score)
run_game()