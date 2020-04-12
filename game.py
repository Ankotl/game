import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship

import game_function as gf


def run_game():
    pygame.init()
    game_set = Settings()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption('Game Covid-19')
    ship = Ship(game_set, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_set, screen, ship, aliens)

    while True:
        gf.check_events(game_set, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullet(bullets)
        gf.update_aliens(game_set, aliens)
        gf.update_screen(game_set, screen, ship, aliens, bullets)


run_game()

