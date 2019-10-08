class Settings():

    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船速度设置

        self.ship_limit = 3

        # 子弹设置

        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60,60,60)

        #外星人设置

        self.alien_drop_speed = 10

        self.score_scale = 1.5
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏变化的设置"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 1.5

        #初始状态 每个外星人值多少分数
        self.alien_points = 50

        # fleet_direction为1表示向右移动，-1表示左移
        self.fleet_direction = 1

    def increase_speed(self):

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)