import pygame as pg
import random
from ..objects import GameObject

class Threat(GameObject):
    def __init__(self, virus_image, safe_image, is_virus=True):
        # Create surface and set rect
        if is_virus:
            self.image = virus_image
        else:
            self.image = safe_image
        super().__init__(random.randint(0, 1024 - 30), -30, 30, 30, self.image)

        self.isvirus = is_virus
        
    def update(self):
        # Slow down falling speed; change this value to adjust speed
        fall_speed = 2  # Change this value to make it fall slower or faster
        self.rect.y += fall_speed
        
        # Remove threat from group when it goes off screen
        if self.rect.top > 576:
            self.kill()

    def is_virus(self):
        return self.isvirus