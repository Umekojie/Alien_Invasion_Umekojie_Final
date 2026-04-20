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
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h
        
        fleet_w, fleet_h, x_offset, y_offset = self.calculate_offsets(alien_w, screen_w, alien_h, screen_h)
       
       # if(level == 1):
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, screen_w, alien_h, screen_h):
        half_screen = self.settings.screen_h/2
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        return fleet_w,fleet_h,x_offset,y_offset
           


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        fleet_w = (screen_w // alien_w)
        fleet_h = (screen_h/2//alien_h)
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        

        return int(fleet_w), int(fleet_h)
    
            
    def _create_alien(self, current_x, current_y):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                
                self.fleet_direction *= -1
                self._drop_alien_fleet()
                break

    def _drop_alien_fleet(self)-> None:
    
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
            

    def update_fleet(self)-> None:
       self._check_fleet_edges()
       self.fleet.update()


    def draw(self)-> None:
        alien: Alien
        for alien in self.fleet:
            alien.draw_alien()

    #def update(self):
        #temp_speed = self.settings.ship_speed
       # if self.moving_right and self.rect.right < self.boundries.right:
            #self.x += temp_speed
        #if self.moving_left and self.rect.left > self.boundries.left:
           # self.x -= temp_speed
        #self.rect.x = self.x