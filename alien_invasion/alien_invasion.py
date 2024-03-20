import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()  # use sprite.Group() to manage all valid bullets at same time
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        # main game start
        while True:  # listen mouse keyboard event
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)  # use game frame from pygame.time.Clock() set it to 60

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 当玩家点击窗口x，关闭游戏
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
        for bullet in self.bullets.sprites():  # bullets.sprites() 会返回一个列表，包含Bullets 编组所有sprites
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # flip screen every sec
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # right key event
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # right key event
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        # delete disappear bullets on the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # check if bullet hit alien
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True, True) # groupcollide()
        # 函数将一个编组中每个元素的rect与另一个编组中每个元素的rect进行比较

        # create another fleet if all aliens are elimate
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size  # rect.size is Tuple()

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self,x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


# if 代码块，仅当运行该文件时，程序代码才会执行，创建alienInvasion
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
