import pygame as pg
from ..objects import *
from ..scene import Scene
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class MainScene(Scene):
    def start(self):
        self.player = Player(50, 50, 15, 20)
        portal_to_vacuum = InteractiveObject(300, 300, 50, 30, os.path.join(assets_folder, "pixil-frame-0.png"))
        test = GameObject(500, 300, 800, 800, os.path.join(assets_folder, "download.png"))
        self.interactions.add()
        self.obstacles.add(test)
        self.all_sprites.add(portal_to_vacuum, test)

    def handle_events(self, events, keys, dt):
        for interaction in self.interactions:
            interaction.interact(events, self.player)
        self.player.move(keys, dt, self)


    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.player.image, self.player.rect)
        self.all_sprites.draw(screen)