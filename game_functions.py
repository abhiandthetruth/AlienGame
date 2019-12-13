import sys
import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.speed += 0.1
    if event.key == pygame.K_DOWN:
        ship.speed -= 0.1
    if(ship.speed < 0):
        ship.speed = 0

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)    
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(conf, screen, ship):
    screen.fill(conf.bg_color)
    ship.update()
    ship.blitme()
    pygame.display.flip()