import pygame as pg
from .within import within

class Character():
    def __init__(self, size_x, size_y, init_x=0, init_y=0):
        self.pos = {"X": init_x, "Y": init_y}
        self.size = {"X": size_x, "Y": size_y}
        self.speed = 300
    def get_x_pos(self):
        return self.pos["X"]
    def get_y_pos(self):
        return self.pos["Y"]
    def set_x_pos(self, x):
        self.pos["X"] = x
    def set_y_pos(self, y):
        self.pos["Y"] = y
    def get_x_size(self):
        return self.size["X"]
    def get_y_size(self):
        return self.size["Y"]

class Player(Character):
    def move_up(self, dt, scene):
        move = True
        for hitbox in scene.get_hitboxes():
            if within(hitbox, self.pos["X"], self.pos["Y"] - self.speed * dt) or within(hitbox, self.pos["X"] + self.size["X"], self.pos["Y"] - self.speed * dt):
                move = False
        if move:
            self.pos["Y"] = self.pos["Y"] - self.speed * dt
    def move_down(self, dt, scene):
        move = True
        for hitbox in scene.get_hitboxes():
            if within(hitbox, self.pos["X"], self.pos["Y"] + self.speed * dt + self.size["Y"]) or within(hitbox, self.pos["X"] + self.size["X"], self.pos["Y"] + self.speed * dt + self.size["Y"]):
                move = False
        if move:
            self.pos["Y"] = self.pos["Y"] + self.speed * dt
    def move_left(self, dt, scene):
        move = True
        for hitbox in scene.get_hitboxes():
            if within(hitbox, self.pos["X"] - self.speed * dt, self.pos["Y"]) or within(hitbox, self.pos["X"] - self.speed * dt, self.pos["Y"] + self.size["Y"]):
                move = False
        if move:
            self.pos["X"] = self.pos["X"] - self.speed * dt
    def move_right(self, dt, scene):
        move = True
        for hitbox in scene.get_hitboxes():
            if within(hitbox, self.pos["X"] + self.speed * dt + self.size["X"], self.pos["Y"]) or within(hitbox, self.pos["X"] + self.speed * dt + self.size["X"], self.pos["Y"] + self.size["Y"]):
                move = False
        if move:
            self.pos["X"] = self.pos["X"] + self.speed * dt
    def move(self, keys, dt, active_scene):
        if keys[pg.K_w]:
            self.move_up(dt, active_scene)
        if keys[pg.K_a]:
            self.move_left(dt, active_scene)
        if keys[pg.K_s]:
            self.move_down(dt, active_scene)
        if keys[pg.K_d]:
            self.move_right(dt, active_scene)