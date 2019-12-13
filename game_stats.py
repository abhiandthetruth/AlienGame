class GameStats():

    def __init__(self, conf):
        self.conf = conf
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.conf.ship_limit