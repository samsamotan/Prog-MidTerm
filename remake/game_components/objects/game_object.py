import pygame as pg

class GameObject(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None):
        super().__init__()
        self.x = x
        self.y = y
        print(image)
        if image == None:
            print("none")
            self.image = pg.Surface((width, height))
            self.image.fill((255,0,0))
        elif isinstance(image, str):
            self.image = pg.image.load(image)
            print("string")
        else:
            print("not string")
            self.image = image
        self.rect = self.image.get_rect(topleft = (x, y))
