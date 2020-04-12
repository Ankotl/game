import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
import game_function as gf


def run_game():
    pygame.init()
    game_set = Settings()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption('Game Covid-19')
    play_button = Button(game_set, screen, "Play")
    ship = Ship(game_set, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(game_set)
    score = ScoreBoard(game_set, screen, stats)
    gf.create_fleet(game_set, screen, ship, aliens)

    while True:
        gf.check_events(game_set, screen, stats, score, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(game_set, screen, stats, score, ship, aliens, bullets)
            gf.update_aliens(game_set, screen, stats, score, ship, aliens, bullets)

        gf.update_screen(game_set, screen, stats, score, ship, aliens, bullets, play_button)


run_game()

