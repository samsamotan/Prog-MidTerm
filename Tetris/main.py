import pygame, sys
from game import Game
from color import Colors 

#To initialize pygame
pygame.init()

#text to display the score (font family, size)
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("SCORE", True, Colors.white)
next_surface = title_font.render("NEXT", True, Colors.white)
game_over_surface = title_font.render("GAME OVER!", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

#the display surface
#set_mode((width, height))
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

#controls the frame rate of the game; how fast the game will run
clock = pygame.time.Clock()

game = Game()

#make the count of the block going down slower
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

#the game loop-defining a way to stop the game's execution
while True:
    #gets all the events pygame recognizes and puts them in a list
    for event in pygame.event.get():
        #if the event is QUIT, we break out of the while loop
        if event.type == pygame.QUIT:
            pygame.quit()
            #command to exit the game
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate() 
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    #Drawing/the Canvas
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (358, 20, 50, 50))
    screen.blit(next_surface, (368, 180, 50, 50))

    if game.game_over == True: 
        screen.blit(game_over_surface, (318, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, 
                score_value_surface.get_rect(centerx = score_rect.centerx,
                                             centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)
    #for the block to move down on its own

    #take all the changes we made in the objects and draws a picture of them
    pygame.display.update()
    #tick tells the clock how fast the game should run (frames per second)
    clock.tick(60)
n 