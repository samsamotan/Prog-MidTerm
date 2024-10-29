import sys
import pygame as pg
import random
from pathlib import Path
import random
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)

from game_components.generic import scene
from game_components.pacman import virus


class PacmanScene(scene.Scene):
    def __init__(self, *args):
        super().__init__(*args)
        self.viruses = [virus.Virus(15, 20, *self.generate_free_pos(), map = self.map) for _ in range(4)]

    def generate_free_pos(self):
        x = random.randint(1,31)
        y = random.randint(1,15)
        if self.map.get_wallgrid_value(x,y):
            return self.generate_free_pos()
        else:
            return (x*32+8, y*32+6)

    def change_tile(self, x, y):
        self.map.change_wallgrid(x, y)

    def render(self, screen, camera, player, events, mouse_pos, dt):
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
        
        for virus in self.viruses:
            virus.move(dt, self.map)
            pg.draw.rect(screen, (0, 255, 0), (virus.get_x_pos() - camera.get_x_pos(), virus.get_y_pos() - camera.get_y_pos(), virus.get_x_size(), virus.get_y_size()))    
        # flip() the display to put your work on screen
        #pg.display.flip()