import pygame

class DisplayText(pygame.sprite.Sprite):
    def __init__(self, text, color, x, y, size=55, centered=False):
        super().__init__()
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.centered = centered
        self.update_image()

    def update_image(self):
        font = pygame.font.SysFont(None, self.size)
        self.image = font.render(self.text, True, self.color)
        if self.centered:
            self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)