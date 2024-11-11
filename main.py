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
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Computer Conquest")

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
while game_state.update():
    surface = pygame.Surface((1024, 576))
    # Handle events, update the scene, and draw everything on the screen
    scene_manager.handle_events(dt)
    scene_manager.update(camera, surface, dt)
    scene_manager.draw(surface)
    screen.blit(pygame.transform.scale(surface, (screen_width, 720)), (0,40))
    pygame.display.flip()

    # Maintain a 60 FPS frame rate
    dt = clock.tick(60) / 1000

# Quit Pygame once the main loop ends
pygame.quit()