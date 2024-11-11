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
        self.audio_manager.play("background_music_menu",-1)
        self.player = Player(50, 50, 0, 0)
        background = GameObject(0, 0, 1024, 576, os.path.join(assets_folder, "game_menu.png"))
        self.new = InvisibleButton(421, 363, 208, 45, (0,0,0,0))
        self.load = InvisibleButton(421, 418, 208, 45, (0,0,0,0))
        self.quit = InvisibleButton(421, 473, 208, 45, (0,0,0,0))
        self.all_sprites.add(background, self.new, self.load, self.quit)
    
    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and event.buttons[0]):
                if self.new.is_clicked(self.game_state.get_mouse_pos()):
                    self.game_state.passed = False
                    self.game_state.colored = False
                    self.player_pos = (875, 450)
                    self.game_state.save_game()
                    self.scene_manager.start_scene("Opening Scene")
                if self.load.is_clicked(self.game_state.get_mouse_pos()):
                    self.game_state.load_game()
                    if self.game_state.colored:
                        
                        self.scene_manager.start_scene("Main Scene")
                    else:
                        self.scene_manager.start_scene("Opening Scene")
                if self.quit.is_clicked(self.game_state.get_mouse_pos()):
                    pygame.quit()
        self.player.move(self.game_state.get_keys(), dt, self)
    
    def draw(self, screen):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.game_state.camera.apply(sprite.rect))
        screen.blit(self.player.image, self.game_state.camera.apply(self.player.rect))