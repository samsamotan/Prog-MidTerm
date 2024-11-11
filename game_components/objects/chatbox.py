import pygame
from .sprite_map import SpriteMap

class Chatbox:
    def __init__(self, messages, scene, next_scene, font_size=24, width=984, height=80, padding=10):
        self.messages = messages  # List of messages
        self.current_message_index = 0
        self.current_text = ""
        self.typing_index = 0
        self.typing_speed = 2  # Control typing speed
        self.font = pygame.font.Font(None, font_size)
        self.width = width
        self.height = height
        self.padding = padding
        self.typing_complete = False
        self.active = False
        self.lines = []  # To store wrapped lines of the current message
        self.scene = scene
        self.next_scene = next_scene

    def start(self):
        self.current_message_index = 0
        self.typing_index = 0
        self.current_text = ""
        self.typing_complete = False
        self.active = True
        self.wrap_message(self.messages[self.current_message_index])

    def update(self):
        # Typing effect: add letters one by one
        if not self.typing_complete and self.active:
            self.typing_index += self.typing_speed
            full_text = self.messages[self.current_message_index]
            if self.typing_index < len(full_text):
                # Update current text based on typing index
                self.current_text = full_text[:self.typing_index]
                self.wrap_message(self.current_text)
            else:
                self.current_text = full_text
                self.wrap_message(self.current_text)
                self.typing_complete = True

    def next_message(self):
        # Check if typing is complete or force-complete it if not
        if not self.typing_complete:
            # Complete the current message instantly
            full_text = self.messages[self.current_message_index]
            self.current_text = full_text
            self.wrap_message(self.current_text)
            self.typing_complete = True
        else:
            # Move to the next message if typing is already complete
            self.current_message_index += 1
            if self.current_message_index < len(self.messages):
                self.typing_index = 0
                self.typing_complete = False
                self.current_text = ""
                self.wrap_message(self.messages[self.current_message_index])
            else:
                self.active = False  # End of conversation
                self.scene.game_state.player_pos = self.scene.player.get_pos()
                self.scene.audio_manager.pause()
                self.scene.scene_manager.start_scene(self.next_scene)

    def wrap_message(self, message):
        # Wrap text into lines that fit within the chatbox width
        self.lines = []
        words = message.split(' ')
        line = ""
        for word in words:
            test_line = line + word + " "
            if self.font.size(test_line)[0] < self.width - 60:
                line = test_line
            else:
                self.lines.append(line)
                line = word + " "
        if line:
            self.lines.append(line)

    def draw(self, surface):
        # Draw chatbox background
        if self.active:
            pygame.draw.rect(surface, (0, 0, 0), (20, 556 - self.height, self.width, self.height))
            pygame.draw.rect(surface, (255, 255, 255), (20, 556 - self.height, self.width, self.height), 2)

            # Draw wrapped text lines inside the chatbox
            y_offset = 576 - self.height
            for line in self.lines:
                text_surface = self.font.render(line, True, (255, 255, 255))
                surface.blit(text_surface, (60, y_offset))
                y_offset += self.font.get_height() + 3  # Move to the next line
            if self.typing_complete:
                continue_message = self.font.render("Press ENTER to continue", True, (255, 255, 255))
                surface.blit(continue_message, (790, 530))