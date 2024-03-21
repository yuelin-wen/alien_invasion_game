from settings import Settings


class GameStats:
    def __init__(self, ai_game):
        self.score = None
        self.ship_left = None
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0


