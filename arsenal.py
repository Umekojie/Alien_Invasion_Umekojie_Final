"""Arsenal
Josephine Cattell
This file will take the bullet from out bullet file and control it on the screen.
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""
import pygame
from typing import TYPE_CHECKING
from bullet import bullet
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
   
class ShipArsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw_arsenal(self) -> None:
        for bullet in self.arsenal :
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False