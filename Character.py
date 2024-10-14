import pygame
class Character():
    def __init__(self, size_x, size_y, init_x=0, init_y=0):
        self.pos = {"X": init_x, "Y": init_y}
        self.size = {"X": size_x, "Y": size_y}
        self.speed = 300
    def get_x_pos(self):
        return self.pos["X"]
    def get_y_pos(self):
        return self.pos["Y"]
    def get_x_size(self):
        return self.size["X"]
    def get_y_size(self):
        return self.size["Y"]

class Player(Character):
    def move(self, keys, dt, scene):
        if keys[pygame.K_w]:
            move = True
            for object in scene.get_objects():
                if object.is_colliding():
                    if object.within(self.pos["X"], self.pos["Y"] - self.speed * dt) or object.within(self.pos["X"] + self.get_x_size(), self.pos["Y"] - self.speed * dt):
                        move = False
            if move:
                self.pos["Y"] = self.pos["Y"] - self.speed * dt
        if keys[pygame.K_s]:
            move = True
            for object in scene.get_objects():
                if object.is_colliding():
                    if object.within(self.pos["X"], self.pos["Y"] + self.speed * dt + self.get_y_size()) or object.within(self.pos["X"] + self.get_x_size(), self.pos["Y"] + self.speed * dt + self.get_y_size()):
                        move = False
            if move:
                self.pos["Y"] = self.pos["Y"] + self.speed * dt
        if keys[pygame.K_a]:
            move = True
            for object in scene.get_objects():
                if object.is_colliding():
                    if object.within(self.pos["X"] - self.speed * dt, self.pos["Y"]) or object.within(self.pos["X"] - self.speed * dt, self.pos["Y"] + self.get_y_size()):
                        move = False
            if move:
                self.pos["X"] = self.pos["X"] - self.speed * dt
        if keys[pygame.K_d]:
            move = True
            for object in scene.get_objects():
                if object.is_colliding():
                    if object.within(self.pos["X"] + self.speed * dt + self.get_x_size(), self.pos["Y"]) or object.within(self.pos["X"] + self.speed * dt + self.get_x_size(), self.pos["Y"] + self.get_y_size()):
                        move = False
            if move:
                self.pos["X"] = self.pos["X"] + self.speed * dt