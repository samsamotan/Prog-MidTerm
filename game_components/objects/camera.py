import pygame

class Camera:
    def __init__(self, screen):
        self.rect = pygame.Rect(0, 0, screen.get_width(), screen.get_height())

    def update(self, target, scene, screen):
        target_x = target.rect.centerx - screen.get_width() // 2
        target_y = target.rect.centery - screen.get_height() // 2
        self.rect.x = max(0, min(target_x, scene.get_width() - screen.get_width()))
        self.rect.y = max(0, min(target_y, scene.get_height() - screen.get_height()))

    def apply(self, entity):
        return entity.move(-self.rect.x, -self.rect.y)