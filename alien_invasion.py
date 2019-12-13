import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
from game_functions import *
import threading

def init_comp():
    pygame.init()
    conf = Settings()
    screen = pygame.display.set_mode((conf.screen_width, 
    conf.screen_height))
    screen.fill(conf.bg_color)
    pygame.display.set_caption(conf.title)
    ship = Ship(screen)
    bullets = Group()
    return {
        'conf':conf, 
        'screen': screen, 
        'ship': ship, 
        'bullets': bullets
    }

def run_game():
    comp = init_comp()
    while True:
        check_events(comp)
        comp['bullets'].update()
        comp['ship'].update()
        threading.Thread(target=update_screen, args=(comp,)).start()

run_game()