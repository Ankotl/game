import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()


def update_screen(game_set, screen, ship):
    screen.fill(game_set.bg_color)
    ship.blitme()
    pygame.display.flip()
