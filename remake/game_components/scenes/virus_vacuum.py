from ..scene import Scene
from ..objects import *
from ..virus_vaccum.virus_vacuum_map import VirusVacuumMap
import os
import pygame as pg

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class VirusVacuum(Scene):
    def __init__(self, manager):
        width = 1024
        height = 576
        super().__init__(manager, width, height)

    def start(self):
        self.player = Player(50, 50, 15, 20)
        new_game = InteractiveObject(225, 150, 270, 48, self.manager, "Main Menu", os.path.join(assets_folder, "pixil-frame-0.png"))
        new_game.add_action(pg.K_e, "change scene")
        self.game_map = VirusVacuumMap(os.path.join(assets_folder, "edge_spritesheet.png"), 32, 32, 16, 1)
        self.interactions.add(new_game)
        self.all_sprites.add(new_game)
    
    def handle_events(self, events, keys, dt):
        for interaction in self.interactions:
            interaction.interact(events, self.player)
        self.player.move(keys, dt, self, self.obstacles, self.game_map.get_tiles())
    
    def draw(self, screen, camera):
        screen.fill((0,0,0))
        self.all_sprites.draw(screen) 
        self.game_map.draw(screen)
        screen.blit(self.player.image, self.player.rect)