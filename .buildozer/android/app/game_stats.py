class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings=ai_settings
        self.rest_stats()
        self.high_score =0
        self.game_active=False

    def rest_stats(self):
        self.ships_left= self.ai_settings.ship_limit
        self.score =0
    def toggle_pause(self):
        self.game_active = True