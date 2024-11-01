import sys
from pathlib import Path
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)
    
from game_components.generic import spritesheet
import pygame as pg

class SpriteMap():
    def __init__(self, filename, tile_names, tile_width, tile_height, columns, rows):
        self.filename = filename
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.columns = columns
        self.rows = rows
        self.tileset = {}
        self.tiles = pg.sprite.Group()
        self.load_tiles()

    def load_tiles(self):
        tile_ss = spritesheet.SpriteSheet(self.filename)
        tile_images = tile_ss.load_grid([0,0,self.tile_height,self.tile_width], self.columns, self.rows)
        
        for i, name in enumerate(self.tile_names):
            self.tileset[name] = tile_images[i] 

    def get_tiles(self):
        return self.tiles
