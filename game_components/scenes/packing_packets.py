import pygame
from ..objects import *
from ..scene import Scene
from ..packing_packets import *
from ..spritesheet import SpriteSheet
import os
import time

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
GAME_UPDATE = pygame.USEREVENT

class PackingPackets(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)
        self.grid = Grid()  # Initialize the grid attribute
        self.player = Player(0, 0, 0, 0)

        


    def start(self):
        self.audio_manager.play("pass_the_password_music", -1)
        pygame.time.set_timer(GAME_UPDATE, 200)
        self.background = pygame.image.load(os.path.join(assets_folder, "Tetris Background.png"))
        complete = SpriteSheet(os.path.join(assets_folder, "complete.jpg"))
        complete_broken = complete.load_grid((1, 1, 25, 25), 18, 18)
        self.tiles = [[GameObject(520+x*25,60+y*25,25,25,complete_broken[x+y*18]) for x in range(18)] for y in range(18)]
        self.game = Game()
        self.title_font = pygame.font.Font(None, 40)
        self.score_surface = self.title_font.render("SCORE", True, Colors.white)
        self.next_surface = self.title_font.render("NEXT", True, Colors.white)
        self.game_over_surface = self.title_font.render("GAME OVER!", True, Colors.white)
        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.wait = 0
        self.next_rect = pygame.Rect(320, 215, 170, 180)

    def update(self, dt):
        if self.game.game_over == True:
            self.wait += dt
            if self.wait >= 10:
                self.scene_manager.start_scene("Main Scene")

    def handle_events(self, dt):
        if not self.game.game_over:
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

    def draw_translucent_rect(self, screen, color, rect, border_radius=0):
        # Create a temporary surface with per-pixel alpha
        translucent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        
        # Fill the surface with the color and apply the alpha value
        translucent_surface.fill(color)
        
        # Draw the rounded rectangle onto this temporary surface
        pygame.draw.rect(translucent_surface, color, translucent_surface.get_rect(), 0, border_radius)

        # Blit the translucent surface onto the main screen
        screen.blit(translucent_surface, rect)

    def draw(self, screen):
        # Draw the background and grid
        screen.blit(self.background, (0, 0, 1024, 576))
        screen.blit(self.score_surface, (358, 20, 50, 50))
        screen.blit(self.next_surface, (368, 180, 50, 50))
        if self.game.score >=1:
            for x in range(3):
                for y in range(3):
                    self.tiles[x*5][y*5].draw(screen) 
        if self.game.score >=2:
            for x in range(5):
                for y in range(5):
                    self.tiles[x*3][y*3].draw(screen) 
        if self.game.score >=3:
            for x in range(7):
                for y in range(7):
                    self.tiles[x*2][y*2].draw(screen) 
        if self.game.score >=4:
            for x in range(9):
                for y in range(9):
                    self.tiles[x*2][y*2].draw(screen) 
        if self.game.score >=5:
            for x in range(18):
                for y in range(18):
                    self.tiles[x][y].draw(screen)
        self.score_value_surface = self.title_font.render(str(self.game.score), True, Colors.white)
        self.draw_translucent_rect(screen, Colors.white, self.score_rect)
        screen.blit(self.score_value_surface, self.score_value_surface.get_rect(centerx = self.score_rect.centerx, centery = self.score_rect.centery))
        self.draw_translucent_rect(screen, Colors.white, self.next_rect)
        self.game.draw(screen)