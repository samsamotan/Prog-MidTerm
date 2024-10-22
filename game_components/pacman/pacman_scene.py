import sys
import pygame as pg
from pathlib import Path
import random
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)

from game_components.generic import scene

class PacmanScene(scene.Scene):
    def change_tile(self, x, y):
        self.map.change_wallgrid(x, y)

    def render(self, screen, camera, player, events, mouse_pos):
        # background
        screen.fill((0, 0, 0))

        for tile in self.map.get_map():
            screen.blit(tile.get_image(), (tile.get_x_pos(), tile.get_y_pos()))

        # objects
        for object in self.scene_objects:
            screen.blit(object.get_image(), (object.get_x_pos() - camera.get_x_pos(), object.get_y_pos() - camera.get_y_pos()))
            
        for event in events:
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.change_tile(mouse_pos[0]//32, mouse_pos[1]//32)
                self.change_tile(random.randint(1,30), random.randint(1,14))
                self.set_hitboxes()
        highlight = pg.Surface((32,32))
        highlight.fill((255,255,255))
        highlight.set_alpha(70)
        screen.blit(highlight, (mouse_pos[0]//32*32, mouse_pos[1]//32*32))
        # player
        pg.draw.rect(screen, (255, 0, 0), (player.get_x_pos() - camera.get_x_pos(), player.get_y_pos() - camera.get_y_pos(), player.get_x_size(), player.get_y_size()))
       
        # flip() the display to put your work on screen
        pg.display.flip()