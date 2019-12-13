import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
from game_functions import *
import threading

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

def run_game():
    comp = Components()
    while True:
        check_events(comp)
        comp.bullets.update()
        for bullet in comp.bullets.copy():
            if bullet.rect.bottom <= 0:
                comp.bullets.remove(bullet)
        comp.ship.update()
        threading.Thread(target=update_screen, args=(comp,)).start()

run_game()