import pygame
from ..objects import *
from ..scene import Scene
from ..packing_packets import *
from .grid import Grid
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
GAME_UPDATE = pygame.USEREVENT

class PackingPackets(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        super().__init__(scene_manager, game_state, audio_manager)
        width = 1024
        height = 576
        self.grid = Grid()  # Initialize the grid attribute
        self.player = Player(0, 0, 0)
        # Initialize other attributes if necessary

    def start(self):
        pygame.time.set_timer(GAME_UPDATE, 200)
        self.game = Game()
        self.player = Player(0,0,0,0)
        self.title_font = pygame.font.Font(None, 40)
        self.score_surface = self.title_font.render("SCORE", True, Colors.white)
        self.next_surface = self.title_font.render("NEXT", True, Colors.white)
        self.game_over_surface = self.title_font.render("GAME OVER!", True, Colors.white)
        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect = pygame.Rect(320, 215, 170, 180)

    def update(self, dt):
        if self.game.game_over == True: 
            self.scene_manager.start_scene("Main Scene")

    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.KEYDOWN:
                if self.game.game_over == True:
                    self.game.game_over = False
                    self.game.reset()
                if event.key == pygame.K_LEFT and self.game.game_over == False:
                    self.game.move_left()
                if event.key == pygame.K_RIGHT and self.game.game_over == False:
                    self.game.move_right()
                if event.key == pygame.K_DOWN and self.game.game_over == False:
                    self.game.move_down()
                    self.game.update_score(0)
                if event.key == pygame.K_UP and self.game.game_over == False:
                    self.game.rotate() 
            if event.type == GAME_UPDATE and self.game.game_over == False:
                self.game.move_down()

    def draw(self, screen, camera):
        # Draw the background and grid
        screen.blit(pygame.image.load(os.path.join(assets_folder, "Tetris Background.png")), (0, 0))
        self.grid.draw(screen)  # Calls the modified draw method for the grid

        # Adjust the position of the score and next tabs
        score_position = (self.grid.width + 40, 20)  # 40px to the right of the grid
        next_position = (self.grid.width + 40, 120)  # 100px below the score tab

        # Translucent white background for score and next tabs
        pygame.draw.rect(screen, (255, 255, 255, 128), (score_position[0], score_position[1], 100, 50))  # Score tab
        pygame.draw.rect(screen, (255, 255, 255, 128), (next_position[0], next_position[1], 100, 100))  # Next tab

        # Draw the text for score and next tabs
        screen.blit(self.score_surface, score_position)
        screen.blit(self.next_surface, next_position)