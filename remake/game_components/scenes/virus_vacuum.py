from ..scene import Scene
from ..objects import *
import os
import pygame as pg

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class VirusVaccum(Scene):
    def start(self):
        self.player = Player(50, 50, 15, 20)
        new_game = InteractiveObject(225, 150, 270, 48, os.path.join(assets_folder, "new_game.png"))
        new_game.add_action(pg.K_e, self.manager.start_scene("Main Scene"))
        load_game = InteractiveObject(225, 210, 270, 48, os.path.join(assets_folder, "load_game.png"))
        load_game.add_action(pg.K_e, self.manager.start_scene("Main Scene"))
        self.interactions.add(new_game, load_game)
        self.all_sprites.add(new_game, load_game)
    
    def handle_events(self, events, keys, dt):
        for interaction in self.interactions:
            interaction.interact(events, self.player)
        self.player.move(keys, dt, self)
    
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.player.image, self.player.rect)
        self.all_sprites.draw(screen)