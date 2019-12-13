class Settings():

    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"

        #ship configurations
        self.ship_speed = 4

        #bullet configuration
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 7

        #alien configuration
        self.alien_speed_factor = 1
        self.alien_drop_speed = 5
        self.fleet_direction = 1    #1 for right and -1 for left
