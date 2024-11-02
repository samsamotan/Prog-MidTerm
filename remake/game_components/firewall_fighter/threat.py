import pygame as pg
import random
from ..objects import GameObject

class Threat(GameObject):
    def __init__(self, is_virus=True):
        color = (255, 0, 0) if is_virus else (255, 255, 255)
        
        # Create surface and set rect
        self.image = pg.Surface(30, 30)
        self.image.fill(color)
        super().__init__(random.randint(0, 1024 - 30), -30, 30, 30, self.image)
        
    def update(self):
        # Slow down falling speed; change this value to adjust speed
        fall_speed = 2  # Change this value to make it fall slower or faster
        self.rect.y += fall_speed
        
        # Remove threat from group when it goes off screen
        if self.rect.top > 576:
            self.kill()