import sys
from pathlib import Path
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)
    
from game_components.generic import spritesheet
import pygame as pg

class Map():
    def __init__(self, filename, tile_names):
        self.tileset = {}
        self.tile_names = tile_names
        self.filename = filename
        self.load_tiles()
        self.tiles = []
    def load_tiles(self):
        tile_ss = spritesheet.SpriteSheet(self.filename)
        tile_images = tile_ss.load_strip([0,0,32,32], 16)
        
        for tile in range(0, len(self.tile_names)):
            self.tileset.update({self.tile_names[tile]: tile_images[tile]})
    def get_map(self):
        return self.tiles


