from ..objects.interactive_object import InteractiveObject
import pygame as pg

class Button(InteractiveObject):
    def __init__(self, x, y, width, height, text):
        image = pg.Surface((80, 80))
        image.fill((125, 0, 125))
        self.font = pg.font.Font(None, 64)
        number = self.font.render(text, True, (255, 255, 255))
        image.blit(number, number.get_rect(center = image.get_rect().center))
        print("image")
        super().__init__(x, y, width, height, image = image)

