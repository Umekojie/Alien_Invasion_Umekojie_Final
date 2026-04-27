"""Alien Invasion Game
Josephine Cattell
Customizing core player assets and Background
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

import sys
import pygame
from Settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import ShipArsenal

#from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)
        
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)
        
        
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))
        
        
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        # Change 'sounds' to 'sound'
        
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)
        
        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))
        self.impact_sound.set_volume(0.7)
        # Adding game feature
        
       
        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        #self.alien_ = Alien(self, 10, 10)
        self.game_active = False

        self.play_button = Button(self, "Start Game")

    def run_game(self)-> None:
        # game loop
        while self.running:
            self._check_events()
                    #draw the ship then background
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        # Check collision for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            print("Ship hit by alien!")
            self._check_game_status()
        # subtract life 
        # check collision for aliens and bottom of screne
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        
        # check collision of projections and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # updete game stus level
            # update HUD view       
  
    def _check_game_status(self):
    
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

       
    def _reset_level(self)-> None:
        self.ship.arsenal.empty()
        self.alien_fleet.empty()
        self.alien_fleet.create_fleet()
#restart game
    def restart_game(self):
        self.settings.initialize_dynamic_settings()
        #reset game stats
        #update HUD scores
        #reset level
        self._reset_level()
        # recenter ship
        self.ship.center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        self.screen.blit(self.bg,(0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        # Draw HUD
        
        if not self.game_active:
            self.play_button.draw_button()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_click(mouse_pos):
            self.restart_game()
    
    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:        
            if self.ship.fire():
                self.laser_sound.play()
                #self.laser_sound.fadeout(250)
                #play laser sound
            
        elif event.key == pygame.K_q:
            self.ship.moving_left = True
            pygame.quit()
            sys.exit()
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
