import pygame as pg
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
        self.font = pg.font.SysFont(None, 55)

    def start(self):
        self.player = Player(0,0,0,0)

        # Target color (randomly generated)
        self.target_color = [random.randint(0, 255) for _ in range(3)]
        # Current mixed color
        self.current_color = [0, 0, 0]

        # Sliders for R, G, B
        self.sliders = {
            'R': Slider('R', (50, 450), RED),
            'G': Slider('G', (50, 500), GREEN),
            'B': Slider('B', (50, 550), BLUE)
        }
        self.all_sprites.add(*self.sliders.values())
        
        # Buttons
        self.reset_button = Button('Reset', 550, 500, 150, 50, DARK_GRAY, WHITE)
        self.all_sprites.add(self.reset_button)
        
        # Match message (hidden by default)
        self.match_message = DisplayText('Matched!', BLACK, 550, 150)
        self.all_sprites.add(self.match_message)

    def handle_events(self, dt):
        pass
    
    def update(self, dt):
        return super().update(dt)

    def draw(self, screen, camera):
        screen.fill(WHITE)
        print(self.target_color)
        pg.draw.rect(screen, self.target_color, (50, 50, 200, 200), border_radius=15)
        DisplayText('Target Color', BLACK, 50, 270).draw(screen)
        
        pg.draw.rect(screen, self.current_color, (300, 50, 200, 200), border_radius=15)
        DisplayText('Current Color', BLACK, 300, 270).draw(screen)
        
        self.all_sprites.draw(screen)
        
        if self.current_color == self.target_color:
            self.match_message.draw(screen)
