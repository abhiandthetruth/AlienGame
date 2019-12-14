import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, conf, screen):
        super().__init__()
        self.screen = screen
        self.conf = conf
        
        #load the image
        self.image = pygame.image.load('images\\alien.bmp')
        self.rect = self.image.get_rect()

        #start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self, horizontal_increment):
        self.x += ((self.conf.alien_speed_factor + horizontal_increment) 
                    * self.conf.fleet_direction)
                    
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False
