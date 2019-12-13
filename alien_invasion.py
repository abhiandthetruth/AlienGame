import pygame
from components import Components
from game_functions import *
import threading


def run_game():
    comp = Components()
    while True:
        check_events(comp)
        comp.update_bullets()
        comp.ship.update()
        threading.Thread(target=update_screen, args=(comp,)).start()

run_game()