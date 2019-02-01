from settings import Settings
import pygame
from pygame.sprite import Group
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button


class AlienInvasionGame:

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self.settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()

        self.stats = GameStats(self.settings)
        self.play_button = Button(self.settings, self.screen, "Play!")
        gf.create_fleet(self.settings, self.screen, self.aliens, self.ship)
        pygame.display.set_caption(self.settings.caption)

    def run_game(self):
        """Run the Game"""
        while True:
            gf.check_events(self.settings, self.screen, self.stats, self.play_button, self.ship, self.aliens, self.bullets)

            if self.stats.gameActive:
                self.ship.update()
                gf.update_bullets(self.settings, self.screen, self.ship, self.aliens, self.bullets)
                gf.update_aliens(self.settings, self.stats, self.screen, self.aliens, self.ship, self.bullets)

            gf.update_screen(self.settings, self.stats, self.screen, self.ship, self.aliens, self.bullets, self.play_button)


if __name__ == "__main__":
    game = AlienInvasionGame()
    game.run_game()
