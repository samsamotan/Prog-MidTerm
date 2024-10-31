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
        self.make_tilemap()
    def change_wallgrid(self, x, y):
        if self.wallgrid[y][x] == 0:
            self.wallgrid[y][x] = 1
        else:
            self.wallgrid[y][x] = 0
        self.make_tilemap()
    def get_groups(self):
        rows, cols = len(self.wallgrid), len(self.wallgrid[0])
        visited = set()
        all_groups = []

        # Collect all zero cells and group them iteratively
        for x in range(rows):
            for y in range(cols):
                if self.wallgrid[x][y] == 0 and (x, y) not in visited:
                    stack = [(x, y)]
                    group = []

                    # Iterative DFS to find all connected zeros
                    while stack:
                        cx, cy = stack.pop()
                        if (cx, cy) in visited:
                            continue
                        visited.add((cx, cy))
                        group.append((cx, cy))

                        # Add valid neighbors to the stack
                        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                            if 0 <= nx < rows and 0 <= ny < cols and self.wallgrid[nx][ny] == 0 and (nx, ny) not in visited:
                                stack.append((nx, ny))

                    # Add the found group to all_groups
                    all_groups.append(group)

        return all_groups
    def get_wallgrid_value(self, x, y):
        return self.wallgrid[y][x]
    def make_tilemap(self):
        self.tiles = []
        for row in range(len(self.wallgrid)):
            for col in range(len(self.wallgrid[0])):
                if self.wallgrid[row][col] == 1:
                    match self.check_adjacency(row, col):
                        case [True, True, True, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["fourway"], (32*(col)), (32*(row)), True))
                        case [False, True, True, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["topless_threeway"], (32*(col)), (32*(row)), True))
                        case [True, True, True, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["bottomless_threeway"], (32*(col)), (32*(row)), True))
                        case [True, False, True, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["rightless_threeway"], (32*(col)), (32*(row)), True))
                        case [True, True, False, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["leftless_threeway"], (32*(col)), (32*(row)), True))
                        case [False, False, True, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["left_bottom_corner"], (32*(col)), (32*(row)), True))
                        case [False, True, False, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["right_bottom_corner"], (32*(col)), (32*(row)), True))
                        case [True, True, False, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["right_top_corner"], (32*(col)), (32*(row)), True))
                        case [True, False, True, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["left_top_corner"], (32*(col)), (32*(row)), True))
                        case [True, False, False, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["top_cap"], (32*(col)), (32*(row)), True))
                        case [False, True, False, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["right_cap"], (32*(col)), (32*(row)), True))
                        case [False, False, True, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["left_cap"], (32*(col)), (32*(row)), True))
                        case [False, False, False, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["bottom_cap"], (32*(col)), (32*(row)), True))
                        case [False, True, True, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["horizontal"], (32*(col)), (32*(row)), True))
                        case [True, False, False, True]:
                            self.tiles.append(map_tile.MapTile(self.tileset["vertical"], (32*(col)), (32*(row)), True))
                        case [False, False, False, False]:
                            self.tiles.append(map_tile.MapTile(self.tileset["lone"], (32*(col)), (32*(row)), True))
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
                if self.wallgrid[row][col+1] == 1 and col != 31:
                    right = True
            except:
                pass               
            try:
                if self.wallgrid[row+1][col] == 1 and row != 15:
                    bottom = True
            except:
                pass
        return [top, right, left, bottom]
