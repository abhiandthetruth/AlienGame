import sys
import pygame
import threading
from alien import Alien
from settings import Settings

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
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        pygame.mouse.set_visible(False)
        comp.reset()

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(comp, mouse_x, mouse_y)

def check_play_button(comp, mouse_x, mouse_y):
    button_clicked = comp.play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not comp.stats.game_active:
        pygame.mouse.set_visible(False)
        comp.reset()
        
    
def update_screen(comp):
    comp.screen.fill(comp.conf.bg_color)
    for bullet in comp.bullets.sprites():
        bullet.draw_bullet()
    t1 = threading.Thread(target=comp.aliens.draw, args=(comp.screen,))
    t1.start()
    t1.join()
    comp.ship.blitme()
    comp.sb.show_score()
    if not comp.stats.game_active:
        comp.screen.fill(comp.conf.bg_color)
        comp.play_button.draw_button()
    pygame.display.flip()

def get_number_aliens_x(conf, alien_width):
    available_space_x = conf.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return number_aliens_x

def get_number_rows(conf, ship_height, alien_height):
    available_space_y = conf.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_fleet(comp):
    alien = Alien(comp.conf, comp.screen)
    number_aliens_x = get_number_aliens_x(comp.conf, alien.rect.width)
    number_rows = get_number_rows(comp.conf, comp.ship.rect.height,
        alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            comp.create_alien(alien_number, row_number)