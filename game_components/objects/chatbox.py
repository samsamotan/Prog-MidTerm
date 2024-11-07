import pygame
from .sprite_map import SpriteMap

class Chatbox:
    def __init__(self, messages, font_size=24, width=984, height=80, padding=10):
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
        # Move to the next message
        if self.typing_complete:
            self.current_message_index += 1
            if self.current_message_index < len(self.messages):
                self.typing_index = 0
                self.typing_complete = False
                self.current_text = ""
                self.wrap_message(self.messages[self.current_message_index])
            else:
                self.active = False  # End of conversation

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


# class ChatboxBackground(SpriteMap):
#     def __init__(self, sprite_sheet, width, line_height, padding=10):
#         # Load sections of the background from the sprite sheet
#         self.top = sprite_sheet.subsurface((0, 0, 32, 32))
#         self.middle = sprite_sheet.subsurface((0, 32, 32, 32))
#         self.bottom = sprite_sheet.subsurface((0, 64, 32, 32))

#         self.width = width
#         self.line_height = line_height
#         self.padding = padding
#         self.height = 0

#     def update_height(self, num_lines):
#         # Calculate the total height based on the number of lines
#         self.height = self.padding * 2 + num_lines * self.line_height

#     def draw(self, surface, x, y):
#         # Draw the top section
#         surface.blit(self.top, (x, y))
#         for i in range(1, (self.height // 32) - 1):
#             surface.blit(self.middle, (x, y + i * 32))  # Middle section repeats
#         surface.blit(self.bottom, (x, y + (self.height // 32 - 1) * 32))  # Bottom section
