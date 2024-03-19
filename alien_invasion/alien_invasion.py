import sys
import pygame
from ship import Ship
from settings import Settings


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()  # set game frame
        self.settings = Settings()  # from my settings module

        # set screen display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # self points to the instance of AlienInvasion

    def run_game(self):
        # main game start
        while True:  # listen mouse keyboard event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # reset background color every flip
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # flip screen every sec
            pygame.display.flip()
            self.clock.tick(60)  # use game frame from pygame.time.Clock() set it to 60


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
