import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Start Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
slot_box_color = (200, 200, 255, 150)  # Semi-transparent color for the box

# Load background map image
background = pygame.image.load("remake/assets/map2.png")  # Replace with your file path
background = pygame.transform.scale(background, (800, 600))

# Font settings
large_font = pygame.font.Font(None, 120)  # For "START"
small_font = pygame.font.Font(None, 72)   # For "Save", "Load", "Exit"
back_font = pygame.font.Font(None, 36)    # For back button in save slot screen
slot_name_font = pygame.font.Font(None, 48)  # Smaller font for save slot names

# Game states
MAIN_MENU = "main_menu"
SAVE_SLOTS = "save_slots"
current_state = MAIN_MENU  # Start at the main menu

# Create title text
title_text = "COMPUTER CONQUEST"
title_surface = small_font.render(title_text, True, BLACK)
title_rect = title_surface.get_rect(center=(400, 100))  # Position "START" near the top-center

# Main menu button labels and positions
buttons = ["Start New Game", "Continue", "Exit Game"]
button_rects = []

for i, text in enumerate(buttons):
    text_surf = small_font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(400, 330 + i * 80))  # Adjust spacing for buttons
    button_rects.append((text_surf, text_rect))

# Save slot information (dummy data)
save_slots_info = [
    {"name": " Slot 1", "status": "Empty", "minigame_icons": [], "character_image": None},
    {"name": " Slot 2", "status": "Empty", "minigame_icons": [], "character_image": None},
    {"name": " Slot 3", "status": "Empty", "minigame_icons": [], "character_image": None},
]

# Load placeholder icons and character images
def load_image(path, size):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
    except pygame.error:
        return None  # Handle missing files gracefully

icon_size = (50, 50)  # Icon size for minigames
character_size = (60, 60)  # Character image size

# Placeholder icons (replace with actual paths)
for slot in save_slots_info:
    slot["minigame_icons"] = [load_image(icon, icon_size) for icon in slot["minigame_icons"]]
    if slot["character_image"]:
        slot["character_image"] = load_image(slot["character_image"], character_size)

# Save slot box settings
slot_box_rects = [pygame.Rect(200, 150 + i * 120, 400, 100) for i in range(3)]

# Back button for save slot screen
back_text = "Back"
back_surf = back_font.render(back_text, True, BLACK)
back_rect = back_surf.get_rect(center=(400, 550))  # Position back button at the bottom

# Functions for button actions
def start_new_game():
    print("Starting a new game...")
    # Add logic to initialize or reset game variables here

def continue_game():
    global current_state
    print("Opening save slots...")
    current_state = SAVE_SLOTS  # Switch to the save slots screen

def load_save_slot(slot_index):
    print(f"Loading game from {save_slots_info[slot_index]['name']}...")
    # Add logic to load the selected game slot

def exit_game():
    print("Exiting the game...")
    pygame.quit()
    sys.exit()

# Function to draw save slots with additional info
def draw_save_slots():
    # Draw the same background image used in the main menu
    screen.blit(background, (0, 0))
    
    for i, slot in enumerate(save_slots_info):
        # Draw semi-transparent slot box with rounded corners
        slot_surf = pygame.Surface((400, 100), pygame.SRCALPHA)  # SRCALPHA allows transparency
        slot_surf.fill(slot_box_color)  # Fill with semi-transparent color
        pygame.draw.rect(slot_surf, BLACK, slot_surf.get_rect(), width=2, border_radius=15)  # Border
        
        # Blit the slot box to the main screen with an offset
        screen.blit(slot_surf, (200, 150 + i * 120))
        
        # Draw slot name with smaller font
        name_surf = slot_name_font.render(slot["name"], True, BLACK)
        screen.blit(name_surf, (210, 160 + i * 120))
        
        # Draw minigame icons (grayed out if not complete)
        for j, icon in enumerate(slot["minigame_icons"]):
            if icon:
                icon_x = 210 + j * (icon_size[0] + 5)
                icon_y = 190 + i * 120
                screen.blit(icon, (icon_x, icon_y))
        
        # Draw character image if available
        if slot["character_image"]:
            screen.blit(slot["character_image"], (480, 170 + i * 120))
        
        # Draw status text (e.g., "Incomplete" or "Empty")
        status_surf = back_font.render(slot["status"], True, BLACK)
        screen.blit(status_surf, (400, 160 + i * 120))
    
    # Draw back button
    screen.blit(back_surf, back_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == MAIN_MENU:
                for i, (text_surf, text_rect) in enumerate(button_rects):
                    if text_rect.collidepoint(event.pos):
                        # Call corresponding function based on the button clicked
                        if i == 0:  # "Start New Game" button
                            start_new_game()
                        elif i == 1:  # "Continue" button
                            continue_game()
                        elif i == 2:  # "Exit Game" button
                            exit_game()
            elif current_state == SAVE_SLOTS:
                for i, slot_rect in enumerate(slot_box_rects):
                    if slot_rect.collidepoint(event.pos):
                        load_save_slot(i)
                if back_rect.collidepoint(event.pos):  # Check if back button is clicked
                    current_state = MAIN_MENU  # Go back to main menu

    # Draw the appropriate screen based on the game state
    if current_state == MAIN_MENU:
        screen.blit(background, (0, 0))  # Draw the background image
        screen.blit(title_surface, title_rect)  # Draw the "START" title

        # Draw main menu buttons
        for text_surf, text_rect in button_rects:
            screen.blit(text_surf, text_rect)
    elif current_state == SAVE_SLOTS:
        draw_save_slots()

    pygame.display.flip()

pygame.quit()