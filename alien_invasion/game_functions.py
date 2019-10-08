import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings,screen,ship,states,aliens,bullets,play_button,score):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(ai_settings,screen,event,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,states,ship,aliens,bullets,play_button,score,mouse_x,mouse_y)

def check_keydown_event(ai_settings,screen,event,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_play_button(ai_settings,screen,states,ship,aliens,bullets,play_button,score,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not states.game_active:
        # #让鼠标不可见
        # pygame.mouse.set_visible(False)
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #重置游戏统计信息
        states.reset_states()
        score.prep_score()
        score.prep_level()
        score.prep_ships()
        states.game_active = True

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


def update_screen(ai_settings,screen,ship,bullets,aliens,states,play_button,score):
    """更新屏幕上的图像，并且换到新屏幕"""
    # 绘制背景颜色
    screen.fill(ai_settings.bg_color)

    # 绘制飞船
    ship.blitme()

    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #绘制外星人
    aliens.draw(screen)

    if not states.game_active :
        play_button.draw_button()
    score.show_score()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,bullets,aliens,ship,states,score):

    bullets.update()

    remove_disappear_bullet(bullets)

    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,states,score)


# 删除已经消失在屏幕中的子弹
def remove_disappear_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

# 检查是否有子弹与外星人碰撞，如果存在，就删除相应的子弹与外星人
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,states,score):

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions :
        for aliens in collisions.values():
            states.score += ai_settings.alien_points * len(aliens)
            score.prep_score()
        check_high_score(states,score)
    if len(aliens) == 0:
        #提高等级
        states.level += 1
        score.prep_level()

        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)

def update_aliens(ai_settings,states,screen,aliens,ship,bullets,score):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,states,screen,ship,aliens,bullets,score)

    #检查是否有外星人到达低端
    check_aliens_bottom(ai_settings,states,screen,ship,aliens,bullets,score)

def check_aliens_bottom(ai_settings,states,screen,ship,aliens,bullets,score):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,states,screen,ship,aliens,bullets,score)
            break

def ship_hit(ai_settings,states,screen,ship,aliens,bullets,score):
    if states.ships_left > 0:
        # 减少ship数量并重新绘制ship编组
        states.ships_left -= 1
        score.prep_ships()
        # 清空外星人与子弹列表
        aliens.empty()
        bullets.empty()

        #创建新的外星人，并将飞船放到屏幕低端
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        states.game_active = False


def fire_bullet(ai_settings,screen,ship,bullets):

    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def create_fleet(ai_settings,screen,aliens,ship):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_alien_y = get_number_aliens_y(ai_settings,ship.rect.height,alien.rect.height)

    for alien_number_row in range(number_alien_y):  #行
        for alien_number_col in range(number_alien_x):  #列
            create_alien(ai_settings,screen,aliens,alien_number_row,alien_number_col)

def get_number_aliens_x(ai_settings,alien_width):

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))

    return number_alien_x

def get_number_aliens_y(ai_settings,ship_width,alien_height):

    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_width
    number_alien_y = int(available_space_y / (2 * alien_height))

    return number_alien_y

def create_alien(ai_settings,screen,aliens,alien_number_row,alien_number_col):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number_col
    alien.y = alien_height + 2 * alien_height * alien_number_row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def check_fleet_edges(ai_settings,aliens):

    """当有外星人碰到边缘时，采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):

    """将外星人下移，并调整移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1

def check_high_score(states,score):

    """检查是否产生了最高分"""
    if states.high_score < states.score:
        states.high_score = states.score
        score.prep_high_score()