import pygame
from .color import Colors

class Grid: 
    def __init__(self): 
        self.num_rows = 19
        self.num_cols = 10
        self.cell_size = 30 
#the 2 dimensional array using for loop
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
#7 colors for the blocks; 1 color for the empty block
        self.colors = Colors.get_cell_colors()

#iterates over every cell in the grid and prints out its value row by row with each row printed on a new line
    def print_grid(self): 
        for row in range(self.num_rows): 
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

#to check if the block is inside the grid
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols: 
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    #method to clear out full rows
    #to check if row is full
    def is_row_full(self,row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    #to clear row
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    
    #to move incomplete rows down
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
            
    #drawing the cells of the grid with a specific color
    def draw(self, screen):
    #first, get the value stored in the cell using a nested for loop
    #iterates through each cell in the grid
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                #rect to contain the cell 
                #x coordinate,y coordinate (top left),width,height
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
                            self.cell_size -1, self.cell_size -1)
                 #3 arguments (surface=screen, color, rect)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)