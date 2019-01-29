from settings import Settings
import pygame
from ship import Ship
import game_functions as gf


class AlienInvasionGame:

    def __init__(self):
        """Initialize the settings, screen object, caption and ship object"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self.screen)

    def run_game(self):
        """Run the Game"""
        pygame.init()
        while True:
            gf.check_events()
            gf.update_screen(self.settings, self.screen, self.ship)


newgame = AlienInvasionGame()
newgame.run_game()
