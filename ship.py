import pygame


class Ship():
    def __init__(self, game_set, screen):
        self.screen = screen
        self.game_set = game_set
        self.image = pygame.image.load('images/cov.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_set.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_set.ship_speed_factor
        if self.moving_up and self.rect.bottom > self.screen_rect.bottom/2:
            self.rect.bottom -= self.game_set.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.game_set.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
