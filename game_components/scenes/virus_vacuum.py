from ..scene import Scene
from ..objects import *
from ..virus_vaccum import *
import os
import pygame

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class VirusVacuum(Scene):
    def __init__(self, scene_manager, game_state):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, width, height)

    def start(self):
        self.player = Player(self.width // 2, self.height // 2, 15, 20, speed = 200)
        self.game_map = VirusVacuumMap(os.path.join(assets_folder, "edge_spritesheet.png"), 32, 32, 16, 1)
        viruses = [Virus(self.game_map) for x in range(4)]
        self.highlight = GameObject(-32, -32, 32, 32)
        self.all_sprites = pygame.sprite.Group(viruses, self.highlight)
        self.viruses = pygame.sprite.Group(viruses)
    
    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game_map.change_wallgrid(self.game_state.get_mouse_pos()[0]//32, self.game_state.get_mouse_pos()[1]//32)
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self, self.obstacles, self.game_map.get_tiles())
    
    def update(self, dt):
        for virus in self.viruses:
            if virus.move(dt, self.game_map, self.player):
                virus.kill()
        self.highlight.rect.x = self.game_state.get_mouse_pos()[0]//32*32
        self.highlight.rect.y = self.game_state.get_mouse_pos()[1]//32*32
        if len(self.viruses) == 0:
            self.scene_manager.start_scene("Main Scene")

    def draw(self, screen, camera):
        screen.fill((0,0,0))
        self.game_map.draw(screen)
        self.all_sprites.draw(screen) 
        screen.blit(self.player.image, self.player.rect)