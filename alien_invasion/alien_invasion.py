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
        # 设置全屏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # self points to the instance of AlienInvasion

    def run_game(self):
        # main game start
        while True:  # listen mouse keyboard event
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)  # use game frame from pygame.time.Clock() set it to 60

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # detect keydown event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # detect key up event, when key release
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        # reset background color every flip
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # flip screen every sec
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # right key event
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # right key event
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
