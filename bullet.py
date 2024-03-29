import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game_set, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_set.bullet_width, game_set.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = game_set.bullet_color
        self.speed_factor = game_set.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
