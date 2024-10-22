import pygame, sys
from grid import Grid

#To initialize pygame
pygame.init()
dark_blue = (44, 44, 127)

#the display surface
#set_mode((width, height))
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Packing Packets")

#controls the frame rate of the game; how fast the game will run
clock = pygame.time.Clock()

game_grid = Grid()

#adding values to the grid
game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 17

game_grid.print_grid()

#the game loop-defining a way to stop the game's execution
while True:
    #gets all the events pygame recognizes and puts them in a list
    for event in pygame.event.get():
        #if the event is QUIT, we break out of the while loop
        if event.type == pygame.QUIT:
            pygame.quit()
            #command to exit the game
            sys.exit()
    #the Canvas
    screen.fill(dark_blue)
    game_grid.draw(screen)
    #take all the changes we made in the objects and draws a picture of them
    pygame.display.update()
    #tick tells the clock how fast the game should run (frames per second)
    clock.tick(60)
