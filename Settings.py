"""Settings
Josephine Cattell
This file defines the screen size and all other compoinents as well as the file routing
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

from pathlib import Path

class Settings:
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd()/'Assets'/'images'/'Starbasesnow.png'
        self.difficulty_scale = 1.1
        # ship settings
        self.ship_file = Path.cwd()/'Assets'/'images'/'ship.png'
        self.bg_file = Path.cwd()/'Assets'/'images'/'Starbasesnow.png'
        self.ship_file = Path.cwd()/'Assets'/'images'/'ship.png'
        self.ship_w = 50
        self.ship_h = 50

        # bullet settings
        self.bullet_file = Path.cwd()/'Assets'/'images'/'laserBlast.png'
        self.laser_sound = Path.cwd()/'Assets'/'sound'/'laser.mp3'
        self.impact_sound = Path.cwd()/'Assets'/'sound'/'impactSound.mp3'


        # enemy settings
        self.alien_file = Path.cwd()/'Assets'/'images'/'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)
        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() /'Assets'/'Fonts'/ 'SilkScreen'/ 'Silkscreen-Bold.ttf'
        self.scores_file = Path.cwd()/'Assets'/'file'/'scores.json'
        
        # life indicator settings
        self.life_image_file = Path.cwd()/'Assets'/'images'/'ship.png'
        self.life_image_w = 25
        self.life_image_h = 25

    def initialize_dynamic_settings(self):
        # Ship settings
        self.ship_speed = 5
        self.starting_ship_count = 3
        # Bullet settings
        self.bullet_speed = 7
        self.bullet_amount = 5
        self.bullet_w = 25
        self.bullet_h = 80
        # Enemy settings
        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self .alien_points = 50 # * level?

    def increase_difficulty(self):
        self.ship_speed += self.difficulty_scale
        self.bullet_speed += self.difficulty_scale
        self.fleet_speed += self.difficulty_scale