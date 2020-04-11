import sys
import pygame
from bullet import Bullet
from alien import Alien


def fire_bullet(game_set, screen, ship, bullets):
    if len(bullets) < game_set.bullets_allowed:
        new_bullet = Bullet(game_set, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, game_set, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_set, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(game_set, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_set, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(game_set, alien_width):
    available_space_x = game_set.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_set, ship_height, alien_height):
    available_space_y = (game_set.screen_height - (3 * alien_height) - ship_height)
    numbers_rows = int(available_space_y/(2*alien_height))
    return numbers_rows


def create_alien(game_set, screen, aliens, alien_number, row_number):
    alien = Alien(game_set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_set, screen, ship, aliens):
    alien = Alien(game_set, screen)
    number_aliens_x = get_number_aliens_x(game_set, alien.rect.width)
    number_rows = get_number_rows(game_set, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_set, screen, aliens, alien_number, row_number)


def update_screen(game_set, screen, ship, aliens, bullets):
    screen.fill(game_set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
