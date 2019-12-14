import pygame.font

class Scoreboard():

    def __init__(self, conf, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.conf = conf
        self.stats = stats
        #set the fonts
        self.text_color = (30, 30 , 30)
        self.font = pygame.font.SysFont(None, 48)
        #initialize
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True
            , self.text_color, self.conf.bg_color)
        
        #display at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        high_score_str = "{:,}".format(round(self.stats.high_score,-1))
        self.high_score_image = self.font.render(high_score_str, True, 
            self.text_color, self.conf.bg_color)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
