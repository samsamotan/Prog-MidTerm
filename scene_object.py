import pygame as pg

class SceneObject(pg.sprite.Sprite):
    def __init__(self, image, size_x, size_y, init_x=0, init_y=0, collision = False):
        super().__init__()
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (init_x, init_y)
        self.collision = collision
        self.pos = (init_x, init_y)
        self.hitbox = {"X1": init_x, "X2": init_x + size_x, "Y1": init_y, "Y2": init_y + size_y}
    def get_image(self):
        return self.image
    def is_colliding(self):
        return self.collision
    def within(self, x, y):
        if (x > self.hitbox["X1"] and x < self.hitbox["X2"] and y > self.hitbox["Y1"] and y < self.hitbox["Y2"]):
            return True
        else:
            return False 
    def update(self, camera):
        self.rect.x = self.pos[0] - camera.get_x_pos()
        self.rect.y = self.pos[1] - camera.get_y_pos()
    