from ..scene import Scene
import os
import pygame
from game_components.objects import *

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
person_image = pygame.image.load(os.path.join(assets_folder, "user.png"))
person_image = pygame.transform.scale(person_image, (180, 180))

class StartChoice(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)

    def start(self):
        self.time = 0
        self.font = pygame.font.Font(None, 40)
        self.yes_button = Button("Yes",300,450, 100,50,(0,0,0),(255,255,255))
        self.no_button = Button("No",450,450, 100,50,(0,0,0),(255,255,255))
        self.all_sprites.add(self.yes_button, self.no_button)
    
    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and event.buttons[0]):
                if self.yes_button.is_clicked(self.game_state.get_mouse_pos()):
                    self.scene_manager.start_scene("Color Match")
                if self.no_button.is_clicked(self.game_state.get_mouse_pos()):
                    self.scene_manager.start_scene("Start Scene")

    def draw(self, screen, camera):
        screen.fill((0,0,0))
        image_rect = person_image.get_rect(center=(self.width // 3, self.height // 2))
        screen.blit(person_image, image_rect)
        message_lines = [
            "Before we can enter the computer,",
            "We need to initialize our colors.",
            "Are you Ready?"
        ]

        line_spacing = 40
        for i, line in enumerate(message_lines):
            line_text = self.font.render(line, True, (255, 255, 255))
            line_position = (image_rect.right + 20, image_rect.top + i * line_spacing)
            screen.blit(line_text, line_position)

        self.all_sprites.draw(screen)

