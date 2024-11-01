import pygame as pg

class GameObject(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None):
        super().__init__()
        if image == None:
            self.image = pg.Surface((width, height))
            self.image.fill((255,0,0))
        else:
            self.image = pg.image.load(image)
        self.rect = self.image.get_rect(topleft = (x, y))
    
    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self))
