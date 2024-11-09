# color_match.py
import pygame
import random
import time
from all_games.map_screen import map_screen  # Import the map_screen function

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Match Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Target color (randomly generated)
target_color = [random.randint(0, 255) for _ in range(3)]

# Current mixed color
current_color = [0, 0, 0]

# Define fonts
font = pygame.font.SysFont(None, 55)

# Define button and slider positions and sizes
slider_width = 300
slider_height = 10
slider_radius = 10
sliders = {
    'R': {'pos': (50, 450), 'color': RED},
    'G': {'pos': (50, 500), 'color': GREEN},
    'B': {'pos': (50, 550), 'color': BLUE}
}
button_width, button_height = 50, 50

# Bypass button position and size
bypass_button = pygame.Rect(600, 50, 150, 50)


def draw_text(text, color, x, y, size=55):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    win.blit(img, (x, y))


def draw_slider(label, value, x, y, color):
    pygame.draw.rect(win, GRAY, (x, y, slider_width, slider_height), border_radius=slider_radius)
    pygame.draw.rect(win, color, (x, y, value / 255 * slider_width, slider_height), border_radius=slider_radius)
    pygame.draw.circle(win, color, (int(x + value / 255 * slider_width), y + slider_height // 2), slider_radius)
    draw_text(f'{label}: {value}', BLACK, x + slider_width + 20, y - 10, 35)


def draw_button(text, x, y, width, height, color=GRAY, text_color=BLACK):
    pygame.draw.rect(win, color, (x, y, width, height), border_radius=15)
    draw_text(text, text_color, x + 10, y + 10, 40)


def draw():
    win.fill(WHITE)

    # Draw target color
    pygame.draw.rect(win, target_color, (50, 50, 200, 200), border_radius=15)
    draw_text('Target Color', BLACK, 50, 270)

    # Draw current color
    pygame.draw.rect(win, current_color, (300, 50, 200, 200), border_radius=15)
    draw_text('Current Color', BLACK, 300, 270)

    # Draw sliders
    for label, slider in sliders.items():
        draw_slider(label, current_color['RGB'.index(label)], slider['pos'][0], slider['pos'][1], slider['color'])

        # Draw increment and decrement buttons
        draw_button('+', slider['pos'][0] + slider_width + 50, slider['pos'][1] - 15, button_width, button_height,
                    slider['color'], WHITE)
        draw_button('-', slider['pos'][0] + slider_width + 120, slider['pos'][1] - 15, button_width, button_height,
                    slider['color'], WHITE)

    # Draw reset button
    draw_button('Reset', 550, 500, 150, 50, DARK_GRAY, WHITE)

    # Draw bypass button
    draw_button('Bypass', bypass_button.x, bypass_button.y, bypass_button.width, bypass_button.height, DARK_GRAY, WHITE)

    # Check match
    if current_color == target_color:
        draw_text('Matched!', BLACK, 550, 150)

    pygame.display.update()


def handle_mouse_click(x, y):
    # Handle slider adjustments and buttons
    for label, slider in sliders.items():
        slider_x, slider_y = slider['pos']
        if slider_x <= x <= slider_x + slider_width and slider_y - slider_height <= y <= slider_y + slider_height:
            current_color['RGB'.index(label)] = int((x - slider_x) / slider_width * 255)
            return

        # Check increment and decrement buttons
        if slider_x + slider_width + 50 <= x <= slider_x + slider_width + 100 and slider_y - 15 <= y <= slider_y + 35:
            current_color['RGB'.index(label)] = min(current_color['RGB'.index(label)] + 15, 255)
            return
        if slider_x + slider_width + 120 <= x <= slider_x + slider_width + 170 and slider_y - 15 <= y <= slider_y + 35:
            current_color['RGB'.index(label)] = max(current_color['RGB'.index(label)] - 15, 0)
            return

    # Reset button
    if 550 <= x <= 700 and 500 <= y <= 550:
        current_color[:] = [0, 0, 0]

    # Bypass button - immediately win the game
    if bypass_button.collidepoint(x, y):
        color_match_win_sequence()  # Trigger win sequence for bypass


def black_transition_screen():
    """Displays a black screen for 2 seconds after winning the game."""
    win.fill(BLACK)
    pygame.display.update()
    time.sleep(2)


def open_world_screen():
    """Displays the 'Opens to the New World' screen before moving to map."""
    win.fill(BLACK)
    draw_text("Opens to the New World", WHITE, 150, HEIGHT // 2)
    pygame.display.update()
    time.sleep(3)
    map_screen()  # Call the imported map_screen function from map_screen.py


def color_match_win_sequence():
    """Handles the win sequence for the Color Match game and exits main loop."""
    black_transition_screen()  # Display black screen for 2 seconds
    open_world_screen()  # Show the open world screen, then map


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)  # Limit the frame rate to 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(*event.pos)

        draw()

        # Check if the current color matches the target color
        if current_color == target_color:
            color_match_win_sequence()  # Trigger win sequence if colors match
            run = False  # Exit main loop after win sequence

    pygame.quit()


if __name__ == "__main__":
    main()
