import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game_set, screen):
        super().__init__()
        self.screen = screen
        self.game_set = game_set
        self.image = pygame.image.load('images/septik.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.game_set.alien_speed_factor * self.game_set.fleet_direction)
        self.rect.x = self.x


