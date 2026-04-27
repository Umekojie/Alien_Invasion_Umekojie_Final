"""Game Stats
Josephine Cattell
This file defines the statstics of the game to the main game
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    def __init__(self, game)-> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
      # update score
      self._update_score(collisions)

    def _update_score(self, collisions):
        for aliens in collisions.values():
            self.score += self.settings.alien_points
      # update max score
        self._update_max_score()
        #print(f'Basic: {self.max_score}')

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
           # print(f'Max: {self.max_score}')

      # update high score

    def update_level(self):
        self.level += 1

    