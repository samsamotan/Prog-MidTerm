from ..objects import *
import pygame
import random

DefaultGrid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

class VirusVacuumMap(SpriteMap):
    def __init__(self, filename, tile_width, tile_height, columns, rows, wallgrid=None):
        tile_names = ["left_cap", "top_cap", "bottom_cap", "right_cap", "left_bottom_corner", "left_top_corner", "right_top_corner", "right_bottom_corner", "topless_threeway", "bottomless_threeway", "rightless_threeway", "leftless_threeway", "fourway", "horizontal", "vertical", "lone"]
        super().__init__(filename, tile_names, tile_width, tile_height, columns, rows)
        self.wallgrid = wallgrid or DefaultGrid
        self.tiles = pygame.sprite.Group()
        self.make_tilemap()

    def change_wallgrid(self, x, y):
        """Toggle wallgrid value at (x, y) and update affected tiles in self.tiles."""
        # Toggle the wallgrid value at (x, y)
        self.wallgrid[y][x] = 1 - self.wallgrid[y][x]  # Toggle between 0 and 1

        # Connect any isolated groups of zeros to ensure map consistency
        self.connect_zero_groups()

        # Update the tile at (x, y)
        self.update_tile(x, y)

        # Update the neighboring tiles, as their adjacency might have changed
        for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if 0 <= ny < len(self.wallgrid) and 0 <= nx < len(self.wallgrid[0]):
                self.update_tile(nx, ny)

    def update_tile(self, x, y):
        """Update or remove the tile at (x, y) in the tiles based on wallgrid."""
        tile_position = (y, x)
        tile_found = None
        for tile in self.tiles:
            if (tile.rect.y // 32, tile.rect.x // 32) == tile_position:
                tile_found = tile
                break

        if self.wallgrid[y][x] == 1:
            adjacency = self.check_adjacency(y, x)
            tile_type = self.get_tile_type(adjacency)
            new_tile = SpriteTile(x * 32, y * 32, 32, 32, self.tileset[tile_type])

            if tile_found:
                # Update the existing tile in the sprite group
                tile_found.image = new_tile.image
            else:
                # Add the new tile if it doesn't already exist
                self.tiles.add(new_tile)

        elif tile_found:
            # Remove tile from the group if the wallgrid at (x, y) is now 0
            self.tiles.remove(tile_found)

    def draw(self, screen):
        self.tiles.draw(screen)

    def update(self, dt):
        self.tiles.update(dt)

    def find_all_zero_groups(self):
        """Identify all groups of connected zeros in the wallgrid."""
        rows, cols = len(self.wallgrid), len(self.wallgrid[0])
        visited = set()
        all_groups = []

        for x in range(rows):
            for y in range(cols):
                if self.wallgrid[x][y] == 0 and (x, y) not in visited:
                    stack = [(x, y)]
                    group = []
                    while stack:
                        cx, cy = stack.pop()
                        if (cx, cy) in visited:
                            continue
                        visited.add((cx, cy))
                        group.append((cx, cy))
                        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                            if 0 <= nx < rows and 0 <= ny < cols and self.wallgrid[nx][ny] == 0 and (nx, ny) not in visited:
                                stack.append((nx, ny))
                    all_groups.append(group)
        return all_groups

    def connect_zero_groups(self):
        """Connects separate zero groups by setting intermediate walls to zero."""
        rows, cols = len(self.wallgrid), len(self.wallgrid[0])

        while True:
            # Identify all zero groups in the current self.wallgrid
            zero_groups = self.find_all_zero_groups()
            
            # Stop when there's only one group of zeros
            if len(zero_groups) <= 1:
                break

            min_distance = float('inf')
            closest_pairs = []

            # Find the closest pairs of zeros between different groups
            for i in range(len(zero_groups)):
                for j in range(i + 1, len(zero_groups)):
                    group1, group2 = zero_groups[i], zero_groups[j]
                    
                    for x1, y1 in group1:
                        for x2, y2 in group2:
                            distance = abs(x1 - x2) + abs(y1 - y2)
                            if distance < min_distance:
                                min_distance = distance
                                closest_pairs = [(x1, y1, x2, y2)]
                            elif distance == min_distance:
                                closest_pairs.append((x1, y1, x2, y2))

            # Randomly select a pair among the closest pairs
            x1, y1, x2, y2 = random.choice(closest_pairs)

            # Randomly choose a position along the line between (x1, y1) and (x2, y2)
            if abs(x1 - x2) > abs(y1 - y2):
                best_position = (random.randint(min(x1, x2), max(x1, x2)), y1)
            else:
                best_position = (x1, random.randint(min(y1, y2), max(y1, y2)))

            # Update the matrix by turning the selected `1` into a `0`
            if best_position:
                x, y = best_position
                if self.wallgrid[x][y] == 1:
                    # Update wallgrid and remove or update the wall tile
                    self.wallgrid[x][y] = 0
                    self.update_tile(y, x)

                    # Update neighboring tiles as their adjacency has changed
                    for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                        if 0 <= nx < rows and 0 <= ny < cols:
                            self.update_tile(ny, nx)
                        
    def get_wallgrid_value(self, x, y):
        return self.wallgrid[y][x]

    def make_tilemap(self):
        """Generates the tilemap based on wallgrid."""
        for row in range(len(self.wallgrid)):
            for col in range(len(self.wallgrid[0])):
                if self.wallgrid[row][col] == 1:
                    adjacency = self.check_adjacency(row, col)
                    tile_type = self.get_tile_type(adjacency)
                    self.tiles.add(SpriteTile(col * 32, row * 32, 32, 32, self.tileset[tile_type]))

    def check_adjacency(self, row, col):
        """Check the adjacency of a tile and return [top, right, left, bottom] states."""
        rows, cols = len(self.wallgrid), len(self.wallgrid[0])
        top = row > 0 and self.wallgrid[row - 1][col] == 1
        right = col < cols - 1 and self.wallgrid[row][col + 1] == 1
        left = col > 0 and self.wallgrid[row][col - 1] == 1
        bottom = row < rows - 1 and self.wallgrid[row + 1][col] == 1
        return [top, right, left, bottom]

    def get_tile_type(self, adjacency):
        """Return the appropriate tile type based on adjacency states."""
        match adjacency:
            case [True, True, True, True]:
                return "fourway"
            case [False, True, True, True]:
                return "topless_threeway"
            case [True, True, True, False]:
                return "bottomless_threeway"
            case [True, False, True, True]:
                return "rightless_threeway"
            case [True, True, False, True]:
                return "leftless_threeway"
            case [False, False, True, True]:
                return "left_bottom_corner"
            case [False, True, False, True]:
                return "right_bottom_corner"
            case [True, True, False, False]:
                return "right_top_corner"
            case [True, False, True, False]:
                return "left_top_corner"
            case [True, False, False, False]:
                return "top_cap"
            case [False, True, False, False]:
                return "right_cap"
            case [False, False, True, False]:
                return "left_cap"
            case [False, False, False, True]:
                return "bottom_cap"
            case [False, True, True, False]:
                return "horizontal"
            case [True, False, False, True]:
                return "vertical"
            case [False, False, False, False]:
                return "lone"