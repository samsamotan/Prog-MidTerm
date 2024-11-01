import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Password Sequence")

# Background
background = pygame.image.load('bg.png')

# Colors
WHITE = (255, 255, 255)
PURPLE = (125, 0, 125)
BUTTON_COLOR = (75, 0, 130)

# Fonts - Using Roboto with larger sizes
try:
    font = pygame.font.Font(os.path.join('fonts', 'Roboto-Regular.ttf'), 48)
    number_font = pygame.font.Font(os.path.join('fonts', 'Roboto-Regular.ttf'), 64)
    small_font = pygame.font.Font(os.path.join('fonts', 'Roboto-Regular.ttf'), 28)
except:
    print("Roboto font not found. Using system default font.")
    font = pygame.font.Font(None, 48)
    number_font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 28)

# Generate a random password sequence of 4 digits, ensuring no repetitions
def generate_random_password():
    return random.sample([1, 2, 3, 4], k=4)

# Check how many positions are correct
def check_guess(guess, correct_password):
    return sum(1 for i in range(4) if guess[i] == correct_password[i])

# Draw buttons for numbers
def draw_buttons(number_buttons):
    button_count = 4
    total_buttons_width = button_count * 80
    spacing = 20
    total_width = total_buttons_width + (spacing * (button_count - 1))
    start_x = (WIDTH - total_width) // 2
    
    for i, button in enumerate(number_buttons):
        pygame.draw.rect(screen, PURPLE, button['rect'], border_radius=8)
        text = number_font.render(str(button['value']), True, WHITE)
        text_rect = text.get_rect(center=button['rect'].center)
        screen.blit(text, text_rect)

# Draw the guess history
def draw_history(guess_history):
    history_start_y = HEIGHT - (len(guess_history) * 35) - 50
    for index, (past_guess, correct_count) in enumerate(guess_history):
        guess_text = small_font.render(f"Guess {index + 1}: {''.join(map(str, past_guess))}", True, WHITE)
        feedback_text = small_font.render(f"Correct positions: {correct_count}", True, WHITE)
        screen.blit(guess_text, (50, history_start_y + index * 35))
        screen.blit(feedback_text, (300, history_start_y + index * 35))

# Draw the "Try Again" button
def draw_try_again_button(button_rect):
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=8)
    button_text = font.render("Try Again", True, WHITE)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

# Main game function
def main():
    running = True
    correct_password = generate_random_password()
    
    button_size = 80
    spacing = 20
    total_width = (button_size * 4) + (spacing * 3)
    start_x = (WIDTH - total_width) // 2
    start_y = 100
    
    number_buttons = [
        {'rect': pygame.Rect(start_x + i * (button_size + spacing), start_y, button_size, button_size), 
         'value': i + 1} for i in range(4)
    ]
    
    try_again_button_rect = pygame.Rect((WIDTH // 2) - 100, (HEIGHT // 2) + 50, 200, 60)
    
    guess = []
    feedback_message = ""
    guess_history = []
    max_tries = 5
    won = False
    game_over = False

    while running:
        screen.blit(background, (0, 0))

        if won:
            victory_message = font.render(f"You guessed the password: {''.join(map(str, correct_password))}", True, WHITE)
            victory_rect = victory_message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(victory_message, victory_rect)
        elif game_over:
            # Display the game-over message
            game_over_text = font.render(f"Game Over! The correct password was: {''.join(map(str, correct_password))}", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(game_over_text, game_over_rect)
            # Draw the "Try Again" button
            draw_try_again_button(try_again_button_rect)
        else:
            draw_buttons(number_buttons)
            guess_text = font.render("Your guess: " + "".join(map(str, guess)), True, WHITE)
            guess_text_rect = guess_text.get_rect(center=(WIDTH // 2, start_y + button_size + 40))
            screen.blit(guess_text, guess_text_rect)
            feedback_text = font.render(feedback_message, True, WHITE)
            feedback_rect = feedback_text.get_rect(center=(WIDTH // 2, start_y + button_size + 90))
            screen.blit(feedback_text, feedback_rect)
            draw_history(guess_history)
            tries_left_text = font.render(f"Tries left: {max_tries - len(guess_history)}", True, WHITE)
            tries_left_rect = tries_left_text.get_rect(center=(WIDTH // 2, start_y + button_size + 140))
            screen.blit(tries_left_text, tries_left_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_over and try_again_button_rect.collidepoint(event.pos):
                    # Reset the game state
                    correct_password = generate_random_password()
                    guess = []
                    feedback_message = ""
                    guess_history = []
                    won = False
                    game_over = False
                elif not won and not game_over:
                    for button in number_buttons:
                        if button['rect'].collidepoint(event.pos) and button['value'] not in guess:
                            guess.append(button['value'])
                            if len(guess) == 4:
                                correct_positions = check_guess(guess, correct_password)
                                if correct_positions == 4:
                                    won = True
                                else:
                                    feedback_message = f"{correct_positions} numbers in the correct position."
                                guess_history.append((guess[:], correct_positions))
                                guess = []
                                if len(guess_history) >= max_tries and not won:
                                    game_over = True

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
