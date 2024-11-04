import pygame as pg
import random
from ..objects import GameObject

class Bullet(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image = image)
        
    def update(self):
        # Slow down falling speed; change this value to adjust speed
        bullet_speed = 10  # Change this value to make it rise slower or faster
        self.rect.y -= bullet_speed
        
        # Remove threat from group when it goes off screen
        if self.rect.top < 0:
            self.kill()