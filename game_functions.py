import sys
import pygame


def check_events():
    """
    respond to keypresses and game events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('thanks for playing, bitch')
            sys.exit()


def update_screen(settings,screen,ship):
    """
    Update images on the screen and flip to the new screen
    :param settings: game settings imported from settings.py
    :param screen: screen objects
    :param ship: ship object
    :return: updated screen
    """
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()


