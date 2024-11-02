import pygame as pg

class HealthBar(pg.sprite.Sprite):
    def __init__(self, max_health, screen_width, color=(255, 0, 0), size=(30, 30), margin=10):
        super().__init__()
        self.max_health = max_health
        self.current_health = max_health
        self.color = color
        self.size = size
        self.margin = margin

        # Calculate the total width needed for all health boxes
        total_width = max_health * size[0] + (max_health - 1) * margin
        self.image = pg.Surface((total_width, size[1] + 2 * margin), pg.SRCALPHA)
        self.rect = self.image.get_rect(topright=(screen_width - margin, margin))

        # Initial draw
        self.update_image()

    def update_health(self, health):
        """Update the health value and refresh the image."""
        self.current_health -= health
        self.update_image()  # Refresh the image to reflect the new health value

    def update_image(self):
        """Draw the health units on the image surface."""
        self.image.fill((0, 0, 0, 0))  # Clear the image (with transparency if using SRCALPHA)
        
        for i in range(self.current_health):
            # Calculate x_position for each health box within the image width
            x_position = i * (self.size[0] + self.margin)
            pg.draw.rect(self.image, self.color, (x_position, self.margin, *self.size))
    
    def get_current_health(self):
        return self.current_health