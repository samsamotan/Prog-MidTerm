import pygame as pg

class Scene:
    def __init__(self, manager):
        self.manager = manager
        self.obstacles = pg.sprite.Group()
        self.interactions = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

    def get_obstacle(self):
        return self.obstacles

    def start(self):
        pass

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass