import pygame as pg
from .game_object import GameObject

class InteractiveObject(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None):
        super().__init__(x, y, width, height, image)
        self.actions = {}

    def add_action(self, key, function):
        self.actions[key] = function

    def interact(self, events, player):
        if self.rect.colliderect(player.rect):
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key in self.actions:
                        self.actions[event.key]()