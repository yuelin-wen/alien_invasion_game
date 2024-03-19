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

        # ship not move when start
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1 # moving right add 1 pixel
        if self.moving_left:
            self.rect.x -= 1 # moving left minus 1 pixel

    def blitme(self):
        # set ship at specific position
        self.screen.blit(self.image, self.rect)
