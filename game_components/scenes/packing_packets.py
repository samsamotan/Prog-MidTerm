import pygame
from ..objects import *
from ..scene import Scene
from ..packing_packets import *
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
GAME_UPDATE = pygame.USEREVENT

class PackingPackets(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)
        self.grid = Grid()  # Initialize the grid attribute
        self.player = Player(0, 0, 0, 0)
        # Initialize other attributes if necessary

    def start(self):
        pygame.time.set_timer(GAME_UPDATE, 200)
        self.game = Game()
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
                if event.key == pygame.K_UP and self.game.game_over == False:
                    self.game.rotate()
            if event.type == GAME_UPDATE and self.game.game_over == False:
                self.game.move_down()

    def draw(self, screen, camera):
        screen.blit(pygame.image.load(os.path.join(assets_folder,"Tetris Background.png")),(0,0,1024,576))
        screen.blit(self.score_surface, (358, 20, 50, 50))
        screen.blit(self.next_surface, (368, 180, 50, 50))

        self.score_value_surface = self.title_font.render(str(self.game.score), True, Colors.white)
        pygame.draw.rect(screen, Colors.light_blue, self.score_rect, 0, 10)
        screen.blit(self.score_value_surface, 
            (self.score_rect.centerx - self.score_value_surface.get_rect().centerx, 
            self.score_rect.centery - self.score_value_surface.get_rect().centery))
        pygame.draw.rect(screen, Colors.light_blue, self.next_rect, 0, 10)
        self.game.draw(screen)
