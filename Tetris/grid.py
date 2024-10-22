import pygame

class Grid: 
    def __init__(self): 
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 
#the 2 dimensional array using for loop
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
#7 colors for the blocks; 1 color for the empty block
        self.colors = self.get_cell_colors()

#iterates over every cell in the grid and prints out its value row by row with each row printed on a new line
    def print_grid(self): 
        for row in range(self.num_rows): 
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

#list of all the colors
    def get_cell_colors(self):

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]


    #drawing the cells of the grid with a specific color
    def draw(self, screen):
    #first, get the value stored in the cell using a nested for loop
    #iterates through each cell in the grid
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                #rect to contain the cell 
                #x coordinate,y coordinate (top left),width,height
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1,
                            self.cell_size -1, self.cell_size -1)
                 #3 arguments (surface=screen, color, rect)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)




