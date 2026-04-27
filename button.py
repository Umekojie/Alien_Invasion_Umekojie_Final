"""Button
Josephine Cattell
This file will house the button class for the game
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:

    def __init__(self,game: 'AlienInvasion',msg)->None:
        self.game = game
        self.screen = game.screen
        self.boundries = self.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font (self.settings.font_file, 
            self.settings.button_font_size)
        # button size
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundries.center
        self._prep_msg(msg)

    def _prep_msg (self, msg)-> None:
        self.msg_image = self.font.render(msg, True, self.settings.text_color,None)
# antialiasing 
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
# check mouse collision
    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    