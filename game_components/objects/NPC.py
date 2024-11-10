import pygame
import sys
import math
from .chatbox import Chatbox

# NPC Class
class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, messages):
        super().__init__()
        self.image = pygame.Surface((width, height))  # Placeholder for the NPC image
        self.image.fill((0, 0, 0, 100))  # Red color as NPC placeholder
        self.rect = self.image.get_rect(topleft=(x, y))
        self.chatbox = Chatbox(messages)
        self.in_proximity = False
        self.font = pygame.font.Font(None, 32)  # Font for the "E" prompt

    def update(self, player_pos):
        # Check if player is in proximity and toggle the interaction prompt
        distance = math.hypot(player_pos[0] - self.rect.x, player_pos[1] - self.rect.y)
        self.in_proximity = distance < 100  # Show letter if within 100 pixels

    def start_conversation(self):
        # Start conversation if player is in proximity
        if self.in_proximity:
            self.chatbox.start()

    def draw_prompt(self, surface, camera):
        # Draw interaction prompt (letter "E") above NPC if in proximity
        if self.in_proximity:
            prompt_text = self.font.render("E", True, (160, 32, 240))  # Purple color for "E"
            surface.blit(prompt_text, camera.apply((self.rect)).move(60,-10))  # Display above the NPC

    def draw_chatbox(self, surface):
        # Draw the chatbox if active
        if self.chatbox.active:
            self.chatbox.draw(surface)