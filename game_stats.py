class GameStats():
    def __init__(self, game_set):
        self.game_set = game_set
        self.game_active = False
        self.high_score = 0
        self.resets_stats()

    def resets_stats(self):
        self.ships_left = self.game_set.ship_limit
        self.score = 0
        self.level = 1