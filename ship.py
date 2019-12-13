import pygame
from settings import Settings
class Ship():

    def __init__(self, screen):
        self.conf = Settings()
        self.screen = screen
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)
        self.speed = self.conf.ship_speed


    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.center = self.screen_rect.centerx