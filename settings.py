class Settings:
    """A class to store all of the settings for my game"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings

        self.screen_width = 600
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        self.caption = 'AHHH FUCK ALIENS!!!'

        # Ship Settings

        self.ship_speed = 1.5

        # Bullet Settings

        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 0, 230, 230
        self.max_bullets = 3

        # Alien Settings

        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # 1 is right, -1 is left
        self.fleet_direction = 1
