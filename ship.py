import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        # ship initial position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image
        self.image = pygame.image.load('images/space_ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # new ship in bottom screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store rect.x load into x
        self.x = float(self.rect.x)

        # ship not move when start
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # moving right add 1 pixel
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed  # moving left minus 1 pixel

        # update rect base on self.x
        self.rect.x = self.x

    def blitme(self):
        # set ship at specific position
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
