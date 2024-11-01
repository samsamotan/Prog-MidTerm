import pygame as pg
from .game_object import GameObject

class Player(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None):
        super().__init__(x, y, width, height, image)
        self.speed = 300

    def move(self, keys, dt, scene):
        initial_x, initial_y = self.rect.x, self.rect.y

        if keys[pg.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pg.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pg.K_s]:
            self.rect.y += self.speed * dt
        if keys[pg.K_d]:
            self.rect.x += self.speed * dt

        for obstacle in scene.get_obstacle():
            if self.rect.colliderect(obstacle.rect):
                self.rect.x, self.rect.y = initial_x, initial_y