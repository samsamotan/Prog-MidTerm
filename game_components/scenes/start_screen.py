from ..scene import Scene
from ..objects import *
import os
import pygame

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class StartScreen(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 2000
        height = 1000
        super().__init__(scene_manager, game_state, audio_manager, width, height)
        
    def start(self):
        self.player = Player(50, 50, 15, 20)
        background = GameObject(0, 0, 1024, 576, os.path.join(assets_folder, "game_menu.png"))
        self.new= InvisibleButton(421, 363, 208, 45)
        self.load = InvisibleButton(421, 418, 208, 45)
        self.quit = InvisibleButton(421, 473, 208, 45)
        #load_game = InteractiveObject(225, 210, 270, 48, self.scene_manager, "Main Menu", "Main Scene", os.path.join(assets_folder, "load_game.png"))
        #load_game.add_action(pygame.K_e, "change scene")
        self.all_sprites.add(background, self.new, self.load, self.quit)
    
    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and event.buttons[0]):
                if self.new.is_clicked(self.game_state.get_mouse_pos()):
                    self.scene_manager.start_scene("Main Scene")
                
                if self.quit.is_clicked(self.game_state.get_mouse_pos()):
                    pygame.quit()
        self.player.move(self.game_state.get_keys(), dt, self)
    
    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))