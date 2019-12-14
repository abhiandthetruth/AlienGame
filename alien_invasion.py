import pygame
from components import Components
from game_functions import *
import threading

def run_game():
    comp = Components()
    create_fleet(comp)
    while True:
        check_events(comp)
        if comp.stats.game_active:
            comp.update_bullets()
            comp.update_ship()
            comp.update_aliens()
            if len(comp.aliens) == 0:
                create_fleet(comp)
        update_screen(comp)

run_game()