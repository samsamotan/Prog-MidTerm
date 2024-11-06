import pygame as pg

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Slider(pg.sprite.Sprite):
    def __init__(self, label, pos, color):
        super().__init__()
        self.label = label
        self.x, self.y = pos
        self.color = color
        self.width = 300
        self.height = 10
        self.radius = 10
        self.value = 0
        self.update_image()

    def update_image(self):
        # Create a blank surface to represent the slider
        self.image = pg.Surface((self.width + 50, self.height + 20), pg.SRCALPHA)
        pg.draw.rect(self.image, GRAY, (0, 10, self.width, self.height), border_radius=self.radius)
        pg.draw.rect(self.image, self.color, (0, 10, self.value / 255 * self.width, self.height), border_radius=self.radius)
        pg.draw.circle(self.image, self.color, (int(self.value / 255 * self.width), self.height // 2 + 10), self.radius)
        
        # Draw the label and value text
        font = pg.font.SysFont(None, 35)
        label_text = font.render(f'{self.label}: {self.value}', True, BLACK)
        self.image.blit(label_text, (self.width + 10, 0))
        
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def set_value(self, value):
        self.value = max(0, min(255, value))
        self.update_image()