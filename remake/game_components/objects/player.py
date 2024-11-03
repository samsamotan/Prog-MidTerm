import pygame as pg
from .game_object import GameObject

class Player(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None, speed = 300):
        super().__init__(x, y, width, height, image)
        self.speed = speed
        self.velocity = pg.Vector2(0, 0)

    def move(self, keys, dt, scene, *groups, vertical_movement = True, horizontal_movement = True):
        self.velocity.x = (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * self.speed * dt
        self.velocity.y = (keys[pg.K_DOWN] - keys[pg.K_UP]) * self.speed * dt

        #Horizontal movement
        if horizontal_movement:
            self.rect.x += self.velocity.x
            for group in groups:
                for obstacle in group:
                    if self.rect.colliderect(obstacle.rect):
                        if self.velocity.x > 0:  # Moving right
                            self.rect.right = obstacle.rect.left
                        elif self.velocity.x < 0:  # Moving left
                            self.rect.left = obstacle.rect.right

        # Vertical movement
        if vertical_movement:
            self.rect.y += self.velocity.y
            for group in groups:
                for obstacle in group:
                    if self.rect.colliderect(obstacle.rect):
                        if self.velocity.y > 0:  # Moving down
                            self.rect.bottom = obstacle.rect.top
                        elif self.velocity.y < 0:  # Moving up
                            self.rect.top = obstacle.rect.bottom

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > scene.get_width() - self.rect.width:
            self.rect.x = scene.get_width() - self.rect.width
        if self.rect.y > scene.get_height() - self.rect.height:
            self.rect.y = scene.get_height() - self.rect.height