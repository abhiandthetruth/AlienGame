import pygame
from components import Components
from game_functions import *
import threading


def run_game():
    comp = Components()
    create_fleet(comp)
    while True:
        check_events(comp)
        comp.update_bullets()
        comp.ship.update()
        update_screen(comp)
        #threading.Thread(target=update_screen, args=(comp,)).start()

run_game()