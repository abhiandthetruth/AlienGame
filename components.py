import pygame
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from alien import Alien
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
        self.aliens = Group()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def fire_bullets(self):
        if len(self.bullets) < self.conf.bullets_allowed:
            new_bullet = Bullet(self.conf, self.screen, self.ship)
            self.bullets.add(new_bullet)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self.conf, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)