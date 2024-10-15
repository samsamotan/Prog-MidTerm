import map_tile
import spritesheet
import pygame

class Map():
    def __init__(self, filename, tile_names):
        self.tileset = {}
        self.tile_names = tile_names
        self.filename = filename
        self.load_tiles()
        self.tiles = []
        print(self.tileset.keys())
    def load_tiles(self):
        tile_ss = spritesheet.SpriteSheet(self.filename)
        tile_images = tile_ss.load_strip([0,0,16,16], 16)
        
        for tile in range(0, len(self.tile_names)):
            self.tileset.update({self.tile_names[tile]: tile_images[tile]})
    def render(self, screen):
        screen.fill('black')
        for tile in self.tiles:
            tile.blitme(screen)


DefaultGrid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

class PacmanMap(Map):
    def __init__(self, *args, wallgrid = DefaultGrid):
        super().__init__(*args)
        self.wallgrid = wallgrid
        self.make_tile_map()
    def make_tile_map(self):
        for row in range(len(self.wallgrid)):
            for col in range(len(self.wallgrid[0])):
                match self.check_adjacency(row, col):
                    case [True, True, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["fourway"],1+(16*(col)),1+(16*(row))))
                    case [False, True, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["topless_threeway"],1+(16*(col)),1+(16*(row))))
                    case [True, True, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["bottomless_threeway"],1+(16*(col)),1+(16*(row))))
                    case [True, False, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["rightless_threeway"],1+(16*(col)),1+(16*(row))))
                    case [True, True, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["leftless_threeway"],1+(16*(col)),1+(16*(row))))
                    case [False, False, True, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["left_bottom_corner"],1+(16*(col)),1+(16*(row))))
                    case [False, True, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["right_bottom_corner"],1+(16*(col)),1+(16*(row))))
                    case [True, True, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["right_top_corner"],1+(16*(col)),1+(16*(row))))
                    case [True, False, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["left_top_corner"],1+(16*(col)),1+(16*(row))))
                    case [True, False, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["top_cap"],1+(16*(col)),1+(16*(row))))
                    case [False, True, False, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["right_cap"],1+(16*(col)),1+(16*(row))))
                    case [False, False, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["left_cap"],1+(16*(col)),1+(16*(row))))
                    case [False, False, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["bottom_cap"],1+(16*(col)),1+(16*(row))))
                    case [False, True, True, False]:
                        self.tiles.append(map_tile.MapTile(self.tileset["horizontal"],1+(16*(col)),1+(16*(row))))
                    case [True, False, False, True]:
                        self.tiles.append(map_tile.MapTile(self.tileset["vertical"],1+(16*(col)),1+(16*(row))))
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
