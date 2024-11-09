# menu.py
import pygame
import time
import sys
from all_games.color_match import main

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, GRAY, BLACK = (255, 255, 255), (100, 100, 100), (0, 0, 0)

# Set up the screen and font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Computer Conquest")
font = pygame.font.Font(None, 40)

# Load images
person_image = pygame.image.load("assets/user.png")
person_image = pygame.transform.scale(person_image, (180, 180))
good_luck_image = pygame.image.load("assets/user.png")
good_luck_image = pygame.transform.scale(good_luck_image, (180, 180))

# Button rectangles
yes_button = pygame.Rect(300, 450, 100, 50)
no_button = pygame.Rect(450, 450, 100, 50)

# Load sounds
pygame.mixer.init()
loading_sound = pygame.mixer.Sound("assets/loading_game.mp3")
background_music = "assets/Goblins_Den_(Regular).wav"

# Define colors and font
title_font = pygame.font.Font(None, 60)

def gaming_loading_screen():
    """Displays the loading screen with a loading bar and sound."""
    loading_sound.play()

    for i in range(101):
        screen.fill(BLACK)
        title_text = title_font.render("Computer Conquest", True, WHITE)
        screen.blit(title_text, (200, 200))
        pygame.draw.rect(screen, GRAY, (150, 300, 500, 40))
        pygame.draw.rect(screen, WHITE, (150, 300, 5 * i, 40))
        loading_text = font.render(f"Loading... {i}%", True, WHITE)
        screen.blit(loading_text, (320, 360))
        pygame.display.flip()
        time.sleep(0.03)

    loading_sound.stop()

def birthday_welcome_screen():
    """Displays the birthday welcome screen for 4 seconds and starts background music."""
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)

    screen.fill(BLACK)
    image_rect = person_image.get_rect(center=(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
    screen.blit(person_image, image_rect)

    message_lines = [
        "Hi Shawn! Happy 7th Birthday",
        "and Welcome to your First",
        "Computer!"
    ]

    line_spacing = 40
    for i, line in enumerate(message_lines):
        line_text = font.render(line, True, WHITE)
        line_position = (image_rect.right + 20, image_rect.top + i * line_spacing)
        screen.blit(line_text, line_position)

    pygame.display.flip()
    time.sleep(4)
    start_game_screen()

def start_game_screen():
    """Displays the start game screen with 'Yes' and 'No' options."""
    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(person_image, (300, 150))
        message_text = font.render("Ready to start the game?", True, WHITE)
        message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, 400))
        screen.blit(message_text, message_rect)

        pygame.draw.rect(screen, WHITE, yes_button)
        pygame.draw.rect(screen, WHITE, no_button)
        yes_text = font.render("Yes", True, BLACK)
        no_text = font.render("No", True, BLACK)
        screen.blit(yes_text, (yes_button.x + 30, yes_button.y + 10))
        screen.blit(no_text, (no_button.x + 30, no_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.collidepoint(event.pos):
                    print("Yes clicked - Going to Good Luck screen...")
                    good_luck_screen()
                    running = False
                elif no_button.collidepoint(event.pos):
                    print("No clicked - Exiting the game...")
                    pygame.quit()
                    sys.exit()

def good_luck_screen():
    """Displays a 'Great and Good Luck' message before starting the game."""
    screen.fill(BLACK)
    image_rect = good_luck_image.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    screen.blit(good_luck_image, image_rect)

    message_text = font.render("Great and Good Luck!", True, WHITE)
    message_rect = message_text.get_rect(left=image_rect.right + 20, centery=image_rect.centery)
    screen.blit(message_text, message_rect)

    pygame.display.flip()
    time.sleep(4)

    main()  # Redirect to color_game screen
