import pygame as pg

class GameObject(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image = None):
        super().__init__()
        self.x = x
        self.y = y
        if image == None:
            self.image = pg.Surface((width, height))
            self.image.fill((255,255,255))
            self.image.set_alpha(70)
        elif isinstance(image, str):
            self.image = pg.image.load(image)
        else:
            self.image = image
        self.rect = self.image.get_rect(topleft = (x, y))
