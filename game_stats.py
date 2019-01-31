class GameStats:
    """Tracks the stats in Alien Invasion"""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.gameActive = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_lives

