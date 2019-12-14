from settings import Settings

class GameStats():

    def __init__(self, conf):
        self.conf = conf
        self.game_active = False
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):   
        self.ships_left = self.conf.ship_limit
        self.score = 0