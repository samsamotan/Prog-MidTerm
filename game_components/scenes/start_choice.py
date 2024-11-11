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
        self.typing_index = 0  # Typing effect index
        self.typing_speed = 0.02  # Adjust speed as desired
        self.time_since_last_character = 0
        self.displaying_no_message = False
        self.message_index = 1  # Track the current index for no_messages

    def start(self):
        self.time = 0
        self.font = pygame.font.Font(None, 40)
        self.yes_button = Button("Yes", 300, 450, 100, 50, (0, 0, 0), (255, 255, 255))
        self.no_button = Button("No", 450, 450, 100, 50, (0, 0, 0), (255, 255, 255))
        self.all_sprites.add(self.yes_button, self.no_button)
        
        # List of messages, each containing multiple lines
        self.messages = [
            ["Before we can enter the computer,", "We need to initialize our colors.", "Are you ready?"],
            ["Maybe you need more time.", "Think it over carefully."],
            ["Take your time, no rush.", "We're in no hurry."],
            ["Are you sure you’re not ready?", "This could be important."],
            ["A wise tiny old green man once said:", "Play or Play not, there is no try."],
            ["Why would you even press no.", "Like seriously, what's the point?"],
            ["Come on, let's get moving."],
            ["Any day now..."], 
            ["Seriously, any day."],
            ["You don’t get it, do you?", "It's might be a yes or no question,", "but the only right answer is YES!"],
            ["This is getting ridiculous.", "You're holding up the line."],
            ["This is your last chance.", "Don’t test my patience."],
            ["Fine. We’re done waiting.", "This conversation is over."]
        ]
        
        # Initialize with the first message
        self.current_message = self.messages[0]
        self.current_line = 0
        self.current_text = ""  # Text being typed out
        self.typing_complete = False

    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and event.buttons[0]):
                if self.yes_button.is_clicked(self.game_state.get_mouse_pos()):
                    self.audio_manager.pause()
                    self.scene_manager.start_scene("Color Match")
                if self.no_button.is_clicked(self.game_state.get_mouse_pos()):
                    # Set up for typing the next "No" message
                    self.displaying_no_message = True
                    self.current_message = self.messages[self.message_index]
                    
                    # Cycle to the next no_message for the next "No" press
                    self.message_index = self.message_index + 1
                    if self.message_index >= len(self.messages):
                        self.audio_manager.pause()
                        self.scene_manager.start_scene("Start Scene")
                    
                    # Reset typing effect variables
                    self.current_line = 0
                    self.current_text = ""
                    self.typing_index = 0
                    self.typing_complete = False

    def update_typing_effect(self, dt):
        if not self.typing_complete:
            self.time_since_last_character += dt
            if self.time_since_last_character >= self.typing_speed:
                self.time_since_last_character = 0
                line = self.current_message[self.current_line]
                self.typing_index += 1
                
                # Add next character to the typing line
                if self.typing_index <= len(line):
                    self.current_text = line[:self.typing_index]
                else:
                    # Move to the next line or stop typing
                    self.typing_index = 0
                    self.current_line += 1
                    if self.current_line >= len(self.current_message):
                        self.typing_complete = True  # No more lines left to type
                    else:
                        self.current_text = ""  # Reset for next line

    def draw(self, screen):
        screen.fill((0, 0, 0))
        image_rect = person_image.get_rect(center=(self.width // 3, self.height // 2))
        screen.blit(person_image, image_rect)

        # Draw typing effect line by line
        line_spacing = 40
        y_offset = image_rect.top
        for i in range(self.current_line):
            # Render completed lines
            line_text = self.font.render(self.current_message[i], True, (255, 255, 255))
            screen.blit(line_text, (image_rect.right + 20, y_offset))
            y_offset += line_spacing

        # Render the current typing line if typing is not complete
        if not self.typing_complete:
            current_line_text = self.font.render(self.current_text, True, (255, 255, 255))
            screen.blit(current_line_text, (image_rect.right + 20, y_offset))
        else:
            # Render any remaining lines if typing is complete
            for remaining_line in self.current_message[self.current_line:]:
                line_text = self.font.render(remaining_line, True, (255, 255, 255))
                screen.blit(line_text, (image_rect.right + 20, y_offset))
                y_offset += line_spacing

        # Draw buttons and other sprites
        self.all_sprites.draw(screen)

    def update(self, dt):
        # Update the typing effect each frame
        self.update_typing_effect(dt)
        self.all_sprites.update(dt)