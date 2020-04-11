import pygame
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    pygame.init()
    game_set = Settings()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))

    pygame.display.set_caption('Game')
    ship = Ship(game_set, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_set, screen, ship)


run_game()

