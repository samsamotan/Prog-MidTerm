import pygame
from menu import birthday_welcome_screen  # Import the welcome screen function

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# Screen and font setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Computer Conquest")
font = pygame.font.Font(None, 36)

# Load assets
background_img = pygame.image.load("assets/game_menu.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define button rectangles
start_button = pygame.Rect(260, 340, 250, 50)
continue_button = pygame.Rect(300, 420, 200, 50)
exit_button = pygame.Rect(300, 500, 200, 50)

# Initialize audio
pygame.mixer.init()
background_music = pygame.mixer.Sound("assets/loading_game.mp3")

def game_menu():
    """Displays the main menu with Start, Continue, and Exit buttons."""
    # Play background music when the menu opens
    background_music.play(-1)  # Loop indefinitely

    running = True
    while running:
        if not pygame.get_init():
            break
        screen.blit(background_img, (0, 0))

        # Draw buttons with rounded corners
        pygame.draw.rect(screen, WHITE, start_button, border_radius=15)
        pygame.draw.rect(screen, WHITE, continue_button, border_radius=15)
        pygame.draw.rect(screen, WHITE, exit_button, border_radius=15)

        # Render button text
        start_text = font.render("Start New Game", True, BLACK)
        continue_text = font.render("Continue", True, BLACK)
        exit_text = font.render("Exit", True, BLACK)

        # Draw text on buttons
        screen.blit(start_text, (start_button.x + 20, start_button.y + 10))
        screen.blit(continue_text, (continue_button.x + 35, continue_button.y + 10))
        screen.blit(exit_text, (exit_button.x + 70, exit_button.y + 10))

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    background_music.stop()  # Stop music when navigating away
                    birthday_welcome_screen()  # Navigate to welcome screen
                elif continue_button.collidepoint(event.pos):
                    print("Continue game (feature not yet implemented)")
                elif exit_button.collidepoint(event.pos):
                    running = False

    # Stop background music when exiting the game menu
    background_music.stop()
    pygame.quit()

if __name__ == "__main__":
    try:
        game_menu()
    except pygame.error:
        print("Pygame error encountered. Exiting game.")
