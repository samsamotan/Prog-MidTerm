import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Screen")

# Load assets
map_background = pygame.image.load("assets/map1.png")
map_background = pygame.transform.scale(map_background, (WIDTH, HEIGHT))
sprite_image = pygame.image.load("assets/character1.png") # Add your sprite image here
sprite_image = pygame.transform.scale(sprite_image, (50, 50))  # Resize as needed

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sprite starting position (bottom left corner of green grass area)
sprite_x, sprite_y = 50, HEIGHT - 100  # Adjust based on your map layout

# Movement variables
sprite_speed = 5

# Collision boundaries for obstacles (tree and water areas)
water_rects = [pygame.Rect(0, 400, 200, 200), pygame.Rect(600, 0, 200, 600)]  # Example water areas
tree_rects = [pygame.Rect(150, 200, 100, 100)]  # Example tree area

# Red house boundary
red_house_rect = pygame.Rect(100, 100, 100, 100)  # Adjust based on red house location

# Function to display the map and handle interactions
def map_screen():
    running = True
    while running:
        win.blit(map_background, (0, 0))
        win.blit(sprite_image, (sprite_x, sprite_y))

        # Draw buttons
        pygame.draw.rect(win, BLACK, (650, 500, 100, 50))  # Up button
        pygame.draw.rect(win, BLACK, (650, 550, 100, 50))  # Down button
        pygame.draw.rect(win, BLACK, (600, 550, 50, 50))   # Left button
        pygame.draw.rect(win, BLACK, (750, 550, 50, 50))   # Right button

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 650 <= x <= 750 and 500 <= y <= 550:  # Up button
                    move_sprite(0, -sprite_speed)
                elif 650 <= x <= 750 and 550 <= y <= 600:  # Down button
                    move_sprite(0, sprite_speed)
                elif 600 <= x <= 650 and 550 <= y <= 600:  # Left button
                    move_sprite(-sprite_speed, 0)
                elif 750 <= x <= 800 and 550 <= y <= 600:  # Right button
                    move_sprite(sprite_speed, 0)

        # Check if the sprite touches the red house
        sprite_rect = pygame.Rect(sprite_x, sprite_y, sprite_image.get_width(), sprite_image.get_height())
        if sprite_rect.colliderect(red_house_rect):
            password_game()  # Trigger password game screen

# Function to move the sprite with collision detection
def move_sprite(dx, dy):
    global sprite_x, sprite_y
    new_x, new_y = sprite_x + dx, sprite_y + dy
    sprite_rect = pygame.Rect(new_x, new_y, sprite_image.get_width(), sprite_image.get_height())

    # Check collision with water and tree areas
    if not any(sprite_rect.colliderect(rect) for rect in water_rects + tree_rects):
        sprite_x, sprite_y = new_x, new_y

# Password game screen
def password_game():
    win.fill(WHITE)
    font = pygame.font.SysFont(None, 36)
    message = font.render("Hi! Shawn, you successfully loaded the computer. Now you need to get into it.", True, BLACK)
    win.blit(message, (50, HEIGHT // 2))
    pygame.display.update()
    time.sleep(3)  # Show message for 3 seconds before returning to map

# Run the map screen
if __name__ == "__main__":
    map_screen()
