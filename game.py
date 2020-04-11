import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    game_set = Settings()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))

    pygame.display.set_caption('Game')
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            screen.fill(game_set.bg_color)
            ship.blitme()
            if event == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()

