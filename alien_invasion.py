import pygame
from components import Components
from game_functions import *
from time import sleep
import threading

def run_game():
    comp = Components()
    create_fleet(comp)
    while True:
        check_events(comp)
        if comp.stats.game_active:
            t1 = threading.Thread(target = comp.update_bullets())
            t2 = threading.Thread(target = comp.update_ship())
            t3 = threading.Thread(target = comp.update_aliens())
            t1.start()
            t2.start()
            t3.start()
            if len(comp.aliens) == 0:
                create_fleet(comp)
            sleep(0.001)
            t1.join()
            t2.join()
            t3.join()
        update_screen(comp)

run_game()