class Settings:
    """A class to store all settings for alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (199, 10, 10)
        self.bullets_allowed = 5

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (4, 1, 36)
        self.ship_speed = 1.25