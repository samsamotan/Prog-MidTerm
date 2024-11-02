import pygame as pg
import random
from ..objects import GameObject

class Threat(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill((255, 255, 0))  # Yellow bullets
        super().__init__(x, y, 5, 10, self.image)
        
    def update(self):
        # Slow down falling speed; change this value to adjust speed
        bullet_speed = 10  # Change this value to make it rise slower or faster
        self.rect.y -= bullet_speed
        
        # Remove threat from group when it goes off screen
        if self.rect.bottom < 0:
            self.kill()