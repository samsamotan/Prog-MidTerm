import pygame

class DisplayText(pygame.sprite.Sprite):
    def __init__(self, text, color, x, y, size=55):
        super().__init__()
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.update_image()

    def update_image(self):
        font = pygame.font.SysFont(None, self.size)
        self.image = font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)