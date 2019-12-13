import pygame
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from settings import Settings

class Components():
    
    def __init__(self):
        pygame.init()
        self.conf = Settings()
        pygame.display.set_caption(self.conf.title)
        self.screen = pygame.display.set_mode((self.conf.screen_width, 
                    self.conf.screen_height))
        self.screen.fill(self.conf.bg_color)
        self.ship = Ship(self.screen)
        self.bullets = Group()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def fire_bullets(self):
        if len(self.bullets) < self.conf.bullets_allowed:
            new_bullet = Bullet(self.conf, self.screen, self.ship)
            self.bullets.add(new_bullet)
