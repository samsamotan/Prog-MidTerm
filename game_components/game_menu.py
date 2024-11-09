import pygame
import time
from menu import birthday_welcome_screen  # Import the welcome screen function

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, GRAY, BLACK = (255, 255, 255), (100, 100, 100), (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Computer Conquest")

background_img = pygame.image.load("assets/game_menu.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)

# Define button rectangles
start_button = pygame.Rect(260, 340, 250, 50)
continue_button = pygame.Rect(300, 420, 200, 50)
exit_button = pygame.Rect(300, 500, 200, 50)

# Load sound
pygame.mixer.init()
loading_sound = pygame.mixer.Sound("assets/Goblins_Dance_(Battle).wav")

def game_menu():
    """Displays the main menu with Start, Continue, and Exit buttons."""
    # Play loading sound at the beginning of the game menu
    loading_sound.play(-1)  # -1 loops the sound indefinitely until stopped

    running = True
    while running:
        if not pygame.get_init():
            break
        screen.blit(background_img, (0, 0))

        pygame.draw.rect(screen, WHITE, start_button, border_radius=15)
        pygame.draw.rect(screen, WHITE, continue_button, border_radius=15)
        pygame.draw.rect(screen, WHITE, exit_button, border_radius=15)

        start_text = font.render("Start New Game", True, BLACK)
        continue_text = font.render("Continue", True, BLACK)
        exit_text = font.render("Exit", True, BLACK)

        screen.blit(start_text, (start_button.x + 20, start_button.y + 10))
        screen.blit(continue_text, (continue_button.x + 35, continue_button.y + 10))
        screen.blit(exit_text, (exit_button.x + 70, exit_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    loading_sound.stop()  # Stop the audio when navigating away
                    birthday_welcome_screen()  # Navigate to welcome screen
                elif continue_button.collidepoint(event.pos):
                    print("Continue game (feature not yet implemented)")
                elif exit_button.collidepoint(event.pos):
                    running = False

    loading_sound.stop()  # Ensure sound stops when exiting the game
    pygame.quit()

if __name__ == "__main__":
    try:
        game_menu()
    except pygame.error:
        print("Pygame error encountered. Exiting game.")
