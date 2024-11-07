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
        background = GameObject(0, 0, 1024, 576, os.path.join(assets_folder, "Game Menu.png"))
        a = InvisibleButton(421, 363, 208, 45)
        b = InvisibleButton(421, 413, 208, 45)
        c = InvisibleButton(421, 463, 208, 45)
        #load_game = InteractiveObject(225, 210, 270, 48, self.scene_manager, "Main Menu", "Main Scene", os.path.join(assets_folder, "load_game.png"))
        #load_game.add_action(pg.K_e, "change scene")
        self.interactions.add(a, b, c)
        self.all_sprites.add(background, a, b, c)
    
    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pg.MOUSEBUTTONDOWN or (event.type == pg.MOUSEMOTION and event.buttons[0]):
                for interaction in self.interactions:
                    if interaction.is_clicked(self.game_state.get_mouse_pos()):
                        print(interaction)
        self.player.move(self.game_state.get_keys(), dt, self)
    
    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))