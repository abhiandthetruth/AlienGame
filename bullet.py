import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, conf, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0 ,conf.bullet_width
        , conf.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = conf.bullet_color
        self.speed_factor = conf.bullet_speed_factor
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)