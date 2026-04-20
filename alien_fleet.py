"""Alien Fleet
Josephine Cattell
This file will take the enemys from the alien flie and multiply them across the screen.
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""


import pygame
from typing import TYPE_CHECKING
from alien import Alien


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
   

class AlienFleet:

    def __init__(self,game:'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self)->None:
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w
        
        #half_screen = self.settings.screen_w
        fleet_w = self.calculate_fleet_size(alien_w, screen_w)
        
        fleet_horizontal_space = fleet_w * alien_w
        x_offset = int((screen_w - fleet_horizontal_space)//2)

        for col in range(fleet_w):
            current_x = alien_w * col + x_offset
            self._create_alien(current_x, 10)


    def calculate_fleet_size(self, alien_w, screen_w):
        fleet_w = (screen_w // alien_w)
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        return fleet_w
            
    def _create_alien(self, current_x, current_y):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self)-> None:
        alien: Alien
        for alien in self.fleet:
            alien.draw_alien()

    def update(self):
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundries.left:
            self.x -= temp_speed
        self.rect.x = self.x