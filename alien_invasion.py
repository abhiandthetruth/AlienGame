import pygame
from ship import Ship
from settings import Settings
from game_functions import *

def init_comp():
    pygame.init()
    conf = Settings()
    screen = pygame.display.set_mode((conf.screen_width, 
    conf.screen_height))
    pygame.display.set_caption(conf.title)
    ship = Ship(screen)
    return {'conf':conf, 'screen': screen, 'ship': ship}

def run_game():
    comp = init_comp()
    while True:
        check_events(comp['ship'])
        update_screen(comp['conf'], comp['screen'], comp['ship'])

run_game()