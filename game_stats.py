"""Game Stats
Josephine Cattell
This file defines the statstics of the game to the main game
This is based on the Eric Matthes 'Python Crash Course' walkthrough and  https://github.com/RedBeard41/alien_Invasion_starter.git
4/12/26"""

class GameStats():

    def __init__(self, ship_limit)-> None:
        self.ships_left = ship_limit
