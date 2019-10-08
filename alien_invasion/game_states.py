class GameStates():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_states()
        self.game_active = False
        self.high_score = 0

    def reset_states(self):

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
