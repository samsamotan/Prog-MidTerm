from ..scene import Scene
from ..objects import *
import os
import pygame as pg

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class MainMenu(Scene):
    def __init__(self, scene_manager, game_state):
        width = 2000
        height = 1000
        super().__init__(scene_manager, game_state, width, height)
        
    def start(self):
        self.player = Player(50, 50, 15, 20)
        new_game = InteractiveObject(225, 150, 270, 48, self.scene_manager, "Main Menu", "Main Scene", os.path.join(assets_folder, "new_game.png"))
        new_game.add_action(pg.K_e, "change scene")
        load_game = InteractiveObject(225, 210, 270, 48, self.scene_manager, "Main Menu", "Main Scene", os.path.join(assets_folder, "load_game.png"))
        load_game.add_action(pg.K_e, "change scene")
        self.interactions.add(new_game, load_game)
        self.all_sprites.add(new_game, load_game)
    
    def handle_events(self, dt):
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self)
    
    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))