import pygame

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, max_value=100):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = 0

    def add_value(self, value):
        # Set the current progress value and clamp it to max_value
        self.current_value = max(0, min(self.current_value+value, self.max_value))

    def draw(self, screen):
        # Calculate the filled width based on the current value
        filled_width = int((self.current_value / self.max_value) * self.width)
        
        # Draw the background (empty portion) of the progress bar
        pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, self.width, self.height), border_radius=10)
        
        # Draw the filled portion of the progress bar
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, filled_width, self.height), border_radius=10)
        
        # Display the percentage text in the center of the progress bar
        font = pygame.font.Font(None, 24)
        percentage = int((self.current_value / self.max_value) * 100)
        text = font.render(f"{percentage}%", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)