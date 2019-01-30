import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent each Alien on the board"""

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien onto the screen"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Update the position of the alien"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

