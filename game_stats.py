from settings import Settings

class GameStats():

    def __init__(self, conf):
        self.conf = conf
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.conf = Settings()        
        self.ships_left = self.conf.ship_limit