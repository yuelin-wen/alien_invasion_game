import sys
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()  # set game frame

        # set screen display
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        #set background color
        self.bg_color = (230,230,230)

    def run_game(self):
        # main game start
        while True:  # listen mouse keyboard event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # reset background color every flip
            self.screen.fill(self.bg_color)
            # flip screen every sec
            pygame.display.flip()
            self.clock.tick(60)  # use game frame from pygame.time.Clock() set it to 60


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
