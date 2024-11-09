import pygame
import pytmx
import os

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
TILE_SIZE = 32

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Map Navigation")

# Paths to the TMX and TSX files
os.path.dirname(__file__) 
tmx_file = os.path.join(os.path.dirname(__file__), "tiledmap.tmx")

# Load the TMX file
try:
    tmx_data = pytmx.load_pygame(tmx_file)
except Exception as e:
    print(f"Error loading TMX file: {e}")
    pygame.quit()
    exit()

# Player settings
player_x = 1
player_y = 1
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill((255, 0, 0))  # Red square for player

# Function to draw the map
def draw_map():
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tmx_data.get_tile_image_by_gid(gid)
                if tile_image:
                    screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))

# Function to move the player
def move_player():
    global player_x, player_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and player_x < (SCREEN_WIDTH // TILE_SIZE) - 1:
        player_x += 1
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and player_y < (SCREEN_HEIGHT // TILE_SIZE) - 1:
        player_y += 1

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    draw_map()  # Draw the map
    screen.blit(player_image, (player_x * TILE_SIZE, player_y * TILE_SIZE))  # Draw the player

    move_player()  # Update player position

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Update the screen

pygame.quit()