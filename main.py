import pygame
from game_components.scene_manager import SceneManager
from game_components.game_state import GameState
from game_components.audio_manager import AudioManager
from game_components.scenes import *
from game_components.objects.camera import Camera
import os

# Initialize Pygame
pygame.init()

# Set up the screen and game variables
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

# Original game surface resolution (16:9 aspect ratio)
game_width, game_height = 1024, 576
game_surface = pygame.Surface((game_width, game_height))

# Calculate the max 16:9 area that fits in the screen
screen_aspect = screen_width / screen_height
target_aspect = 16 / 9

if screen_aspect > target_aspect:
    # Screen is wider than 16:9, so we base scaling on height
    scaled_height = screen_height
    scaled_width = int(scaled_height * target_aspect)
else:
    # Screen is taller than 16:9, so we base scaling on width
    scaled_width = screen_width
    scaled_height = int(scaled_width / target_aspect)

offset_x = (screen_width - scaled_width) // 2
offset_y = (screen_height - scaled_height) // 2

scale_x = scaled_width / game_width
scale_y = scaled_height / game_height

assets_folder = os.path.join(os.path.dirname(__file__), "assets")
camera = Camera(screen)
game_state = GameState(camera)
audio_manager = AudioManager()
scene_manager = SceneManager(game_state, audio_manager)

# Add scenes to the scene manager
scene_manager.add_scene("Start Scene", StartScreen)
scene_manager.add_scene("Main Scene", MainScene)
scene_manager.add_scene("Opening Scene", Opening)
scene_manager.add_scene("Choice Scene", StartChoice)
scene_manager.add_scene("Virus Vacuum", VirusVacuum)
scene_manager.add_scene("Firewall Fighter", FirewallFighter)
scene_manager.add_scene("Pass the Password", PassThePassword)
scene_manager.add_scene("Packing Packets", PackingPackets)
scene_manager.add_scene("Color Match", ColorMatch)

# Start the initial scene
scene_manager.start_scene("Start Scene")

# Set up the game clock for consistent frame rate
clock = pygame.time.Clock()
dt = 0

# Main game loop
while game_state.update(offset_x, offset_y, scale_x, scale_y):
    surface = pygame.Surface((1024, 576))
    # Handle events, update the scene, and draw everything on the screen
    scene_manager.handle_events(dt)
    scene_manager.update(camera, surface, dt)
    scene_manager.draw(surface)
    screen.blit(pygame.transform.scale(surface, (scaled_width, scaled_height)), (offset_x,offset_y))
    pygame.display.flip()

    # Maintain a 60 FPS frame rate
    dt = clock.tick(60) / 1000

# Quit Pygame once the main loop ends
pygame.quit()