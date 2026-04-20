"""Settings
Josephine Cattell
This file defines the screen size and all other compoinents as well as the file routing
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

from pathlib import Path

class Settings:
  def __init__(self):
        self.name: str ='Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800 
        self.FPS = 60
        self.bg_file = Path.cwd()/'Assets'/'images'/'background.png'

        self.ship_file = Path.cwd()/'Assets'/'images'/'Ladyship.png'
        self.bg_file = Path.cwd()/'Assets'/'images'/'background.png'

        self.ship_file = Path.cwd()/'Assets'/'images'/'Ladyship.png'
        self.ship_w = 100
        self.ship_h = 120
        self.starting_ship_count = 3
        self.ship_speed = 5

        self.bullet_file = Path.cwd()/'Assets'/'images'/'rosebullet.png'
        self.laser_sound = Path.cwd()/'Assets'/'sound'/'laser.mp3'
        self.impact_sound = Path.cwd()/'Assets'/'sound'/'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5
        
        self.alien_file = Path.cwd()/'Assets'/'images'/'grub_villan.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.fleet_drop_speed = 40
        