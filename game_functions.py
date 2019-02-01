import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, settings, screen, ship, bullets):
    """Check all keydown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Check all keyup events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, stats, play_button, ship, aliens, bullets):
    """respond to key presses and game events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        reset_game(settings, screen, stats, ship, aliens, bullets)


def reset_game(settings, screen, stats, ship, aliens, bullets):
    stats.reset_stats()
    stats.gameActive = True
    aliens.empty()
    bullets.empty()
    create_fleet(settings, screen, aliens, ship)
    ship.center_ship()


def fire_bullet(settings, screen, ship, bullets):
    """Check if the bullets group is full, if not, create/fire new bullet"""
    if len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(settings, screen, aliens, ship, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)


def update_bullets(settings, screen, ship,  aliens, bullets):
    """Check if bullets have left the screen, destroy if so"""
    bullets.update(bullets)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, aliens, ship, bullets)


def get_number_rows_y(settings, alien_height, ship_height):
    """Calculate how many rows of aliens will be spawned per fleet"""
    available_space_y = settings.screen_height - (alien_height*3) - ship_height
    number_rows_y = int(available_space_y / (alien_height * 2))
    return number_rows_y


def get_number_aliens_x(settings, alien_width):
    """Get the number of aliens that will be allowed on the screen"""
    available_space_x = settings.screen_width - (alien_width * 2)
    num_aliens_x = int(available_space_x / (alien_width * 2))
    return num_aliens_x


def create_alien(screen, settings, aliens, alien_number, row_number):
    """Create a new alien and add it to the aliens group"""
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(settings, screen, aliens, ship):
    """Create a fleet full of aliens"""
    alien = Alien(screen, settings)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows_y(settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen, settings, aliens, alien_number, row_number)


def check_fleet_edges(settings, aliens):
    """Respond appropriately if any alien has reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """Change the direction of each alien in the fleet"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, stats, screen, ship, aliens, bullets):
    """Respond appropriately to a ship being hit by an alien"""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)

    else:
        stats.gameActive = False


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    """Respond appropriately to any alien striking the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(settings, stats, screen, aliens, ship, bullets):
    """Check if an alien is at the edge, then update all aliens positions"""
    check_fleet_edges(settings, aliens)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)


def update_screen(settings, stats, screen, ship, aliens, bullets, play_button):
    """
    Update images on the screen and flip to the new screen
    :param settings: game settings imported from settings.py
    :param screen: screen objects
    :param ship: ship object
    :param bullets: the list of bullets in AlienInvasionGame
    :param aliens: the group of aliens
    :return: nothing - updates the view of the screen
    """
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.gameActive:
        play_button.draw_button()
    pygame.display.flip()






