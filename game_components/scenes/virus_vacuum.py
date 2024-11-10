from ..scene import Scene
from ..objects import *
from ..virus_vaccum import *
import os
import pygame

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class VirusVacuum(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)

        # Initialize sounds
        pygame.mixer.init()

        #Load sounds

        self.background_music = pygame.mixer.music.load(os.path.join(assets_folder, "Donkey Kong Country - Aquatic Ambience [Restored].mp3"))
        pygame.mixer.music.play(-1)


    def start(self):
        self.background = GameObject(0,-35,1024,576, os.path.join(assets_folder, "pacman_game_background.png"))
        self.player = Player(self.width // 2, self.height // 2, 15, 20, speed = 100, image = os.path.join(assets_folder, "cowboy.png"))
        self.game_map = VirusVacuumMap(os.path.join(assets_folder, "edge_spritesheet.png"), 32, 32, 16, 1)
        self.viruses = [Virus(self.game_map, os.path.join(assets_folder, "virus.png")) for x in range(4)]
        self.virus_counter = DisplayText("Viruses Remaining: " + str(len(self.viruses)), (0,0,0), 20, 535, 30)
        self.highlight = GameObject(-32, -32, 32, 32)
        self.all_sprites = pygame.sprite.Group(self.viruses, self.highlight, self.virus_counter)
        self.viruses = pygame.sprite.Group(self.viruses)
    
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
                self.virus_counter.text = "Viruses Remaining: " + str(len(self.viruses))
                self.virus_counter.update_image()
        self.highlight.rect.x = self.game_state.get_mouse_pos()[0]//32*32
        self.highlight.rect.y = self.game_state.get_mouse_pos()[1]//32*32
        if len(self.viruses) == 0:
            self.scene_manager.start_scene("Main Scene")

    def draw(self, screen):
        screen.fill((168,138,113))
        screen.blit(self.background.image, self.background.rect)
        self.game_map.draw(screen)
        self.all_sprites.draw(screen) 
        screen.blit(self.player.image, self.player.rect)