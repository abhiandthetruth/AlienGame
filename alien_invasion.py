import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    conf = Settings()
    
    screen = pygame.display.set_mode((conf.screen_width, 
    conf.screen_height))
    pygame.display.set_caption(conf.title)
    screen.fill(conf.bg_color)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        pygame.display.flip()

run_game()