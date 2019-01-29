from settings import Settings
import pygame
from pygame.sprite import Group
from ship import Ship
import game_functions as gf


class AlienInvasionGame:

    def __init__(self):
        """Initialize the settings, screen object, caption and ship object"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self.settings, self.screen)
        self.bullets = Group()

        pygame.display.set_caption(self.settings.caption)
        pygame.init()

    def run_game(self):
        """Run the Game"""
        while True:
            gf.check_events(self.settings, self.screen, self.ship, self.bullets)
            self.ship.update()
            gf.update_bullets(self.bullets)
            gf.update_screen(self.settings, self.screen, self.ship, self.bullets)


if __name__ == "__main__":
    newgame = AlienInvasionGame()
    newgame.run_game()
