
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship speed setting
        self.ship_speed = 1.5

        # bullet setting
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 means move to right, -1 means move to left
        self.fleet_direction = 1