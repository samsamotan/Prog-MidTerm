# main.py
import pygame
from menu import gaming_loading_screen # Import directly from menu
from game_menu import game_menu
pygame.init()

# Show loading screen first
gaming_loading_screen()

# Go to main menu after loading screen
game_menu()