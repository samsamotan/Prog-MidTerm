import pygame

class ScoreCounter(pygame.sprite.Sprite):
    def __init__(self, x, y, font_size=30, color=(255, 255, 0)):
        super().__init__()
        
        # Initialize score and font
        self.score = 0
        self.font = pygame.font.Font(None, font_size)  # Use the default font
        self.color = color

        # Create the initial image and rect
        self.image = self.font.render(f"Score: {self.score}", True, self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_score(self, amount):
        """Update the score by a specified amount and refresh the display."""
        self.score += amount
        self.image = self.font.render(f"Score: {self.score}", True, self.color)

    def set_score(self, new_score):
        """Set the score to a specific value and refresh the display."""
        self.score = new_score
        self.image = self.font.render(f"Score: {self.score}", True, self.color)

    def reset_score(self):
        """Reset the score to zero and refresh the display."""
        self.score = 0
        self.image = self.font.render(f"Score: {self.score}", True, self.color)