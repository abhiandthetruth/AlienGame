import sys
import pygame


def check_keydown_events(event, comp):
    if event.key == pygame.K_RIGHT:
        comp.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        comp.ship.moving_left = True
    elif event.key == pygame.K_UP:
        comp.ship.speed += 0.1
    elif event.key == pygame.K_DOWN:
        comp.ship.speed -= 0.1
        if comp.ship.speed < 0:
            comp.ship.speed = 0
    elif event.key == pygame.K_SPACE:
        comp.fire_bullets()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(comp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, comp)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, comp.ship)
            
def update_screen(comp):
    comp.screen.fill(comp.conf.bg_color)
    for bullet in comp.bullets.sprites():
        bullet.draw_bullet()
    comp.ship.blitme()
    pygame.display.flip()