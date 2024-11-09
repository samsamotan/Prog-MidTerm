from .color import Colors
import pygame
from .position import Position

# Each block will have a unique ID
class Block: 
    def __init__(self, id=None):  # Add id as a parameter
        self.id = id  # Assign the id to the instance
        # Dictionary to store the occupied cells in the bounding grid for each rotation state
        self.cells = {}
        self.cell_size = 30
#attributes: hold the row and offset the block on the game grid
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

#update the position of the cell by adding the offset to the current
#adding the row and column offset 

    def move(self, rows, columns): 
        self.row_offset += rows
        self.column_offset += columns
#calculate the position of each cell after the offset is applied in a list
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

#for rotating the block
    def rotate(self):
        self.rotation_state += 1
    #resetting back to 0 after maximum rotation states
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x=0, offset_y=0):
        # Retrieves the list of positions for the current rotation state of the tetromino
        tiles = self.get_cell_positions()  # This calls your existing method
        # Drawing a rectangle for each cell
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                    offset_y + tile.row * self.cell_size,
                                    self.cell_size - 1,
                                    self.cell_size - 1)
            # Draw the main black block
            pygame.draw.rect(screen, Colors.black, tile_rect)
            
            # Add light gray pixel details for a 'data packet' effect
            # Top-left pixel detail
            pygame.draw.rect(screen, Colors.light_gray, tile_rect.inflate(-self.cell_size * 0.8, -self.cell_size * 0.8).move(1, 1))
            # Bottom-right pixel detail
            pygame.draw.rect(screen, Colors.light_gray, tile_rect.inflate(-self.cell_size * 0.8, -self.cell_size * 0.8).move(-1, -1))


