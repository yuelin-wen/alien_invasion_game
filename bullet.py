import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # Sprite 可以将游戏相关的元素编组，进而可以操作编组中所有的元素
    def __init__(self, ai_game):
        # manage bullet of ship
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet at (0,0), then set it to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet position into variable
        self.y = float(self.rect.y)

    def update(self):
        # moving bullet to top
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
