"""Alien
Josephine Cattell
This file will create the enemys on the screen
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        super().__init__()
        
        self.screen = game.screen
        self.boundries = game.screen.get_rect()
        self.settings = game.settings

        self.image= pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed
        self.rect.x = self.x

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)