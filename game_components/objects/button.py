import pygame as pg

GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

class Button(pg.sprite.Sprite):
    def __init__(self, text, x, y, width, height, color=GRAY, text_color=BLACK):
        super().__init__()
        self.text = text
        self.color = color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.update_image()

    def update_image(self):
        # Create the button surface with a rounded rectangle and text
        self.image = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.rect(self.image, self.color, (0, 0, self.width, self.height), border_radius=15)
        
        font = pg.font.SysFont(None, 40)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.width // 2, self.height // 2))
        self.image.blit(text_surf, text_rect)
        
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def is_clicked(self, x, y):
        return self.rect.collidepoint(x, y)