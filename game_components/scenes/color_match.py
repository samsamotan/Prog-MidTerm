import pygame
from ..objects import *
from ..color_match import *
from ..scene import Scene
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

class ColorMatch(Scene):
    def __init__(self, scene_manager, game_state):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, width, height)
        # Define fonts
        self.font = pygame.font.SysFont(None, 55)

    def start(self):
        self.player = Player(0,0,0,0)

        self.progress = ProgressBar(650, 150, 300, 30)

        # Target color (randomly generated)
        self.target_color = [random.randint(0, 255) for _ in range(3)]
        # Current mixed color
        self.current_color = [0, 0, 0]

        # Sliders for R, G, B
        self.sliders = {
            'R': Slider('R', (50, 400), RED),
            'G': Slider('G', (50, 450), GREEN),
            'B': Slider('B', (50, 500), BLUE)
        }
        
        # Buttons
        self.reset_button = Button('Reset', 550, 400, 150, 50, DARK_GRAY, WHITE)
        self.submit_button = Button('Submit', 550, 460, 150, 50, DARK_GRAY, WHITE)
        self.interactions.add(self.reset_button, self.submit_button)
        self.all_sprites.add(self.reset_button, self.submit_button)

    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and event.buttons[0]):
                for slider in self.sliders.values():
                    slider.update(event)
                if self.reset_button.is_clicked(self.game_state.get_mouse_pos()):
                    self.current_color = [0,0,0]
                    for slider in self.sliders.values():
                        slider.reset_value()
                if self.submit_button.is_clicked(self.game_state.get_mouse_pos()):
                    self.check_color()
                    self.target_color = [random.randint(0, 255) for _ in range(3)]
                    if self.progress.current_value == 100:
                        self.scene_manager.start_scene("Main Scene")

    def check_color(self):
        value = 0
        for index in range(len(self.current_color)):
            value += 100 - abs(self.current_color[index] - self.target_color[index])
        value /= 10
        self.progress.add_value(value)

    def update(self, dt):
        self.current_color = [self.sliders["R"].value, self.sliders["G"].value, self.sliders["B"].value]

    def draw(self, screen, camera):
        screen.fill(WHITE)

        for slider in self.sliders.values():
            slider.draw(screen)

        self.progress.draw(screen)

        pygame.draw.rect(screen, self.target_color, (50, 50, 200, 200), border_radius=15)
        DisplayText('Target Color', BLACK, 50, 270).draw(screen)
        
        pygame.draw.rect(screen, self.current_color, (300, 50, 200, 200), border_radius=15)
        DisplayText('Current Color', BLACK, 300, 270).draw(screen)
        
        self.all_sprites.draw(screen)
        
        if self.current_color == self.target_color:
            self.match_message.draw(screen)
