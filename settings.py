class Settings():

    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"

        #ship configurations
        self.ship_speed = 4
        self.ship_limit = 2

        #bullet configuration
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 7

        #alien configuration
        self.alien_speed_factor = float(1)
        self.alien_drop_speed = float(20)
        self.alien_points = 50
        self.fleet_direction = 1    #1 for right and -1 for left

        #spedup
        self.speedup_scale = 1.1
        self.score_scale = 1.5
