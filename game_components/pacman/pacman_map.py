import sys
from pathlib import Path
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)
    
from game_components.generic import map_tile
from game_components.generic import map

DefaultGrid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

class PacmanMap(map.Map):
    def __init__(self, *args, wallgrid = DefaultGrid):
        super().__init__(*args)
        self.wallgrid = wallgrid
        self.make_tile_map()
    def make_tile_map(self):
        for row in range(len(self.wallgrid)):
            for col in range(len(self.wallgrid[0])):
                match self.check_adjacency(row, col):
                    case [True, True, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["fourway"],1+(32*(col)),1+(32*(row)), True))
                    case [False, True, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["topless_threeway"],1+(32*(col)),1+(32*(row)), True))
                    case [True, True, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["bottomless_threeway"],1+(32*(col)),1+(32*(row)), True))
                    case [True, False, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["rightless_threeway"],1+(32*(col)),1+(32*(row)), True))
                    case [True, True, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["leftless_threeway"],1+(32*(col)),1+(32*(row)), True))
                    case [False, False, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["left_bottom_corner"],1+(32*(col)),1+(32*(row)), True))
                    case [False, True, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["right_bottom_corner"],1+(32*(col)),1+(32*(row)), True))
                    case [True, True, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["right_top_corner"],1+(32*(col)),1+(32*(row)), True))
                    case [True, False, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["left_top_corner"],1+(32*(col)),1+(32*(row)), True))
                    case [True, False, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["top_cap"],1+(32*(col)),1+(32*(row)), True))
                    case [False, True, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["right_cap"],1+(32*(col)),1+(32*(row)), True))
                    case [False, False, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["left_cap"],1+(32*(col)),1+(32*(row)), True))
                    case [False, False, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["bottom_cap"],1+(32*(col)),1+(32*(row)), True))
                    case [False, True, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["horizontal"],1+(32*(col)),1+(32*(row)), True))
                    case [True, False, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["vertical"],1+(32*(col)),1+(32*(row)), True))
                    case [False, False, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["blank"],1+(32*(col)),1+(32*(row)), False))
    def check_adjacency(self, row, col):
        top, right, left, bottom = False, False, False, False     
        if self.wallgrid[row][col] == 1:
            try:
                if self.wallgrid[row-1][col] == 1 and row != 0:
                    top = True
            except:
                pass             
            try:
                if self.wallgrid[row][col-1] == 1 and col != 0:
                    left = True
            except:
                pass        
            try:
                if self.wallgrid[row][col+1] == 1:
                    right = True
            except:
                pass               
            try:
                if self.wallgrid[row+1][col] == 1:
                    bottom = True
            except:
                pass
        return [top, right, left, bottom]
