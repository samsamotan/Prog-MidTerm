from ..scene import Scene
import os
import pygame

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
person_image = pygame.image.load(os.path.join(assets_folder, "user.png"))
person_image = pygame.transform.scale(person_image, (180, 180))

class Opening(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)

    def start(self):
        self.time = 0
        self.font = pygame.font.Font(None, 40)
    
    def update(self, dt):
        self.time += dt
        if self.time >= 3:
            self.scene_manager.start_scene("Choice Scene")
    
    def draw(self, screen):
        screen.fill((0,0,0))
        image_rect = person_image.get_rect(center=(self.width // 3, self.height // 2))
        screen.blit(person_image, image_rect)

        message_lines = [
            "Hi Shawn! Happy 7th Birthday",
            "and Welcome to your First",
            "Computer!"
        ]

        line_spacing = 40
        for i, line in enumerate(message_lines):
            line_text = self.font.render(line, True, (255, 255, 255))
            line_position = (image_rect.right + 20, image_rect.top + i * line_spacing)
            screen.blit(line_text, line_position)

