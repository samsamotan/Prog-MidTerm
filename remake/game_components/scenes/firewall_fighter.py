import pygame as pg
from ..objects import *
from ..scene import Scene
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

# Game constants
POINTS_TO_LEVEL_UP = 30
HEALTH_MAX = 3

class FirewallFighter(Scene):
    def __init__(self, scene_manager, game_state):
        width = 2000
        height = 1000
        super().__init__(scene_manager, game_state, width, height)  


    def start(self):
        self.player = Player(50, 50, 15, 20)
        self.player_health = HEALTH_MAX
        self.threats = pg.sprite.Group()
        self.bullets = pg.sprite.Group()

    def handle_events(self, dt):
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self, horizontal_movement = False)


    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))