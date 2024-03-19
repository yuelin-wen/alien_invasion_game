import pygame


class Ship:
    def __init__(self, ai_game):
        # ship initial position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image
        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()

        # new ship in bottom screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # set ship at specific position
        self.screen.blit(self.image, self.rect)
