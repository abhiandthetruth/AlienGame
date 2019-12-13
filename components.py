import pygame
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from alien import Alien
from settings import Settings

class Components():
    
    def __init__(self):
        pygame.init()
        self.conf = Settings()
        pygame.display.set_caption(self.conf.title)
        self.screen = pygame.display.set_mode((self.conf.screen_width, 
                    self.conf.screen_height))
        self.screen.fill(self.conf.bg_color)
        self.ship = Ship(self.screen)
        self.bullets = Group()
        self.aliens = Group()

    def update_ship(self):
        self.ship.update()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.handle_collisions()

    def handle_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
            True, True)
        if len(self.aliens) == 0:
            self.bullets.empty()
            self.conf.alien_speed_factor += 0.2
            self.conf.alien_drop_speed += 0.4

    def fire_bullets(self):
        if len(self.bullets) < self.conf.bullets_allowed:
            new_bullet = Bullet(self.conf, self.screen, self.ship)
            self.bullets.add(new_bullet)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self.conf, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    
    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.conf.alien_drop_speed
        self.conf.fleet_direction *= -1