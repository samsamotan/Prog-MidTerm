import pygame
import sys
import math
from .chatbox import Chatbox

# NPC Class
class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, width=0, height=0, messages=["dootdoot"], scene = None, next_scene = None, image = None):
        super().__init__()
        self.animated = False
        if image == None:
            self.image = pygame.Surface((width, height))  # Placeholder for the NPC image
            self.image.fill((0, 0, 0, 100))  # Red color as NPC placeholder
        else:
            self.images = []
            self.sheet = pygame.image.load(image).convert_alpha()  # Using convert_alpha for transparency
            rect = pygame.Rect((1,2,117,132))
            image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()  # Preserve transparency
            image.blit(self.sheet, (0, 0), rect)
            self.images.append(image)
            rect = pygame.Rect((118,2,117,132))
            image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()  # Preserve transparency
            image.blit(self.sheet, (0, 0), rect)
            self.images.append(image)
            self.image = self.images[0]
            print(self.image)
            self.animated = True
        self.current_frame = 0
        self.animation_speed = 1  # Time in seconds per frame
        self.animation_timer = 0
        self.rect = self.image.get_rect(topleft=(x, y))
        self.chatbox = Chatbox(messages, scene, next_scene)
        self.in_proximity = False
        self.font = pygame.font.Font(None, 32)  # Font for the "E" prompt
        self.end_conversation_distance = 300

    def update(self, player_pos, dt):
        if self.animated:
            self.animation_timer += dt
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.images)
                self.image = self.images[self.current_frame]

        # Check if player is in proximity and toggle the interaction prompt
        distance = math.hypot(player_pos[0] - self.rect.x, player_pos[1] - self.rect.y)
        self.in_proximity = distance < 100  # Show letter if within 100 pixels

        if distance > self.end_conversation_distance and self.chatbox.active:
            self.end_conversation()

    def start_conversation(self):
        # Start conversation if player is in proximity
        if self.in_proximity:
            self.chatbox.start()

    def end_conversation(self):
        # End the chatbox conversation
        self.chatbox.active = False
        self.chatbox.current_message_index = 0  # Reset conversation index if desired

    def draw_prompt(self, surface, camera):
        # Draw interaction prompt (letter "E") above NPC if in proximity
        if self.in_proximity:
            prompt_text = self.font.render("E", True, (160, 32, 240))  # Purple color for "E"
            surface.blit(prompt_text, camera.apply(self.rect).move(60,-10))  # Display above the NPC

    def draw_chatbox(self, surface):
        # Draw the chatbox if active
        if self.chatbox.active:
            self.chatbox.draw(surface)