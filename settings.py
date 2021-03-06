class Settings():

    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (240, 248, 255)
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 2
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.aliens_point = 50
        self.score_scale = 1.5


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.aliens_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.aliens_point = int(self.aliens_point * self.score_scale)

