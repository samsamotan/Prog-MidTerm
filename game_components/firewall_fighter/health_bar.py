import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, max_health, screen_width, heart_image_path):
        super().__init__()
        self.max_health = max_health
        self.current_health = max_health
        self.screen_width = screen_width

        # Load and scale the heart image
        self.heart_image = pygame.image.load(heart_image_path)
        self.heart_image = pygame.transform.scale(self.heart_image, (20, 20))  # Scale the heart image to a smaller size
        self.heart_spacing = 5  # Spacing between hearts
        self.image = pygame.Surface((self.max_health * (self.heart_image.get_width() + self.heart_spacing), 
                                     self.heart_image.get_height()), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topright=(self.screen_width - 10, 10))  # Position at top-right corner of the screen

    def update_health(self, amount):
        """Adjust health by amount; decrease if amount is positive, increase if negative."""
        self.current_health = max(0, min(self.max_health, self.current_health - amount))

    def update(self):
        """Redraw hearts based on current health."""
        self.image.fill((0, 0, 0, 0))  # Clear the surface with transparency
        for i in range(self.current_health):
            x = i * (self.heart_image.get_width() + self.heart_spacing)
            self.image.blit(self.heart_image, (x, 0))

    def get_current_health(self):
        return self.current_health

    def draw(self, screen):
        """Draws hearts on the screen representing the current health."""
        for i in range(self.current_health):
            x = self.heart_spacing + (i * (self.heart_image.get_width() + self.heart_spacing))  # Space out hearts
            y = self.heart_spacing  # Position hearts at the top of the screen
            screen.blit(self.heart_image, (x, y))
