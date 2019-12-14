class GameStats():

    def __init__(self, conf):
        self.conf = conf
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.conf.ship_limit