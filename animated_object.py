from game_components.generic import spritesheet
import pygame
from math import floor
class AnimatedObject():
    def __init__(self):
        self.sprite = spritesheet.SpriteSheet("game_components/assets/doot.png")
        self.sprites = self.sprite.load_grid((0, 256, 110, 128), 8, 7)
        self.value = 0
    def render(self, screen, camera):
        screen.blit(self.sprites[floor(self.value)%56], (1500 - camera.get_x_pos(), 800 - camera.get_y_pos()))
        self.value += 0.1
