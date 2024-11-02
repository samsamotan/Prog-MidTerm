import pygame as pg
from ..objects import *
from ..scene import Scene
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class PassThePassword(Scene):
    def __init__(self, scene_manager, game_state):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, width, height)

    def start(self):
        self.player = Player(50, 50, 15, 20)
        portal_to_vacuum = InteractiveObject(300, 300, 50, 30, self.scene_manager, "Main Scene", "Virus Vacuum", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_vacuum.add_action(pg.K_e, "change scene")
        portal_to_vacuum = InteractiveObject(300, 400, 50, 30, self.scene_manager, "Main Scene", "Firewall Fighter", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_vacuum.add_action(pg.K_e, "change scene")
        test = GameObject(500, 300, 800, 800, os.path.join(assets_folder, "download.png"))
        self.interactions.add(portal_to_vacuum)
        self.obstacles.add(test)
        self.all_sprites.add(portal_to_vacuum, test)

    def handle_events(self, dt):
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self)


    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))