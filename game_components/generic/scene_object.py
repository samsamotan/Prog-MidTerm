import pygame as pg

class SceneObject():
    def __init__(self, image, size_x, size_y, init_x=0, init_y=0, collision = False):
        self.pos = {"X": init_x, "Y": init_y}
        try:
            self.image = pg.image.load(image)
        except:
            pass
        self.collision = collision
        self.hitbox = {"X1": init_x, "X2": init_x + size_x, "Y1": init_y, "Y2": init_y + size_y}
    def get_x_pos(self):
        return self.pos["X"]
    def get_y_pos(self):
        return self.pos["Y"]
    def get_image(self):
        return self.image
    def is_colliding(self):
        return self.collision
    def within(self, x, y):
        if (x > self.hitbox["X1"] and x < self.hitbox["X2"] and y > self.hitbox["Y1"] and y < self.hitbox["Y2"]):
            return True
        else:
            return False 
    