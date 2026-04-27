"""HUD
Josephine Cattell
This file defines the HUD for the game to the main game
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

import pygame.font
#from typing import TYPE_CHECKING
#from alien_invasion import AlienInvasion
#if TYPE_CHECKING:
    

class HUD:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = self.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        #self.setup_life_image()
        #self.updatelevel()

    def update_scores(self)-> None:
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self)-> None:
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color,None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self)-> None:
        max_score_str = f'Max Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color,None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self)-> None:
        hi_score_str = f'High Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color,None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundries.centerx, self.padding)

    def draw(self) -> None:
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        