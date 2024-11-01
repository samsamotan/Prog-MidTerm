import random
import pygame as pg

from game_components.firewall_fighter.level2 import SCREEN_HEIGHT, SCREEN_WIDTH

class Character():
    def __init__(self, size_x, size_y, init_x=0, init_y=0):
        self.pos = {"X": init_x, "Y": init_y}
        self.size = {"X": size_x, "Y": size_y}
        self.speed = 300  # Speed in pixels per second

    def get_x_pos(self):
        return self.pos["X"]

    def get_y_pos(self):
        return self.pos["Y"]

    def get_x_size(self):
        return self.size["X"]

    def get_y_size(self):
        return self.size["Y"]

class Player(Character):
    def move_up(self, dt, scene):
        move = True
        for obj in scene.get_objects():
            if obj.is_colliding():
                if obj.within(self.pos["X"], self.pos["Y"] - self.speed * dt) or obj.within(self.pos["X"] + self.size["X"], self.pos["Y"] - self.speed * dt):
                    move = False
        if move:
            self.pos["Y"] -= self.speed * dt

    def move_down(self, dt, scene):
        move = True
        for obj in scene.get_objects():
            if obj.is_colliding():
                if obj.within(self.pos["X"], self.pos["Y"] + self.speed * dt + self.size["Y"]) or obj.within(self.pos["X"] + self.size["X"], self.pos["Y"] + self.speed * dt + self.size["Y"]):
                    move = False
        if move:
            self.pos["Y"] += self.speed * dt

    def move_left(self, dt, scene):
        move = True
        for obj in scene.get_objects():
            if obj.is_colliding():
                if obj.within(self.pos["X"] - self.speed * dt, self.pos["Y"]) or obj.within(self.pos["X"] - self.speed * dt, self.pos["Y"] + self.size["Y"]):
                    move = False
        if move:
            self.pos["X"] -= self.speed * dt

    def move_right(self, dt, scene):
        move = True
        for obj in scene.get_objects():
            if obj.is_colliding():
                if obj.within(self.pos["X"] + self.speed * dt + self.size["X"], self.pos["Y"]) or obj.within(self.pos["X"] + self.speed * dt + self.size["X"], self.pos["Y"] + self.size["Y"]):
                    move = False
        if move:
            self.pos["X"] += self.speed * dt

    def move(self, keys, dt, active_scene):
        if keys[pg.K_w]:  # Move up with W
            self.move_up(dt, active_scene)
        if keys[pg.K_a]:  # Move left with A
            self.move_left(dt, active_scene)
        if keys[pg.K_s]:  # Move down with S
            self.move_down(dt, active_scene)
        if keys[pg.K_d]:  # Move right with D
            self.move_right(dt, active_scene)

# Threat class definition (Viruses and Safe Programs)
class Threat(pg.sprite.Sprite):
    def __init__(self, is_virus=True):
        super().__init__()
        # Set size for threats (viruses and safe programs)
        size = (30, 30)
        
        # Set color based on type (red for viruses, white for safe programs)
        color = (255, 0, 0) if is_virus else (255, 255, 255)
        
        # Create surface and set rect
        self.image = pg.Surface(size)
        self.image.fill(color)
        
        # Initialize position randomly above the screen
        self.rect = self.image.get_rect(center=(random.randint(30, SCREEN_WIDTH - 30), -30))
        
    def update(self):
        # Slow down falling speed; change this value to adjust speed
        fall_speed = 2  # Change this value to make it fall slower or faster
        self.rect.y += fall_speed
        
        # Remove threat from group when it goes off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
