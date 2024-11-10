import pygame
from game_components.scene_manager import SceneManager
from game_components.game_state import GameState
from game_components.audio_manager import AudioManager
from game_components.scenes import *
from game_components.objects.camera import Camera
import os

# Initialize Pygame and the mixer for sound
pygame.init()
pygame.mixer.init()

# Set up the screen and game variables
screen = pygame.display.set_mode((1024, 576))
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

# Load audio files into the audio manager
audio_manager.load("background_music_menu", os.path.join(assets_folder, "Goblins_Dance_(Battle).wav"))
audio_manager.load("start_scene_music", os.path.join(assets_folder, "Undertale Ost_ 087 - Hopes and Dreams.mp3"))
audio_manager.load("main_scene_music", os.path.join(assets_folder, "time_for_adventure.mp3"))
audio_manager.load("virus_vacuum_music", os.path.join(assets_folder, "Donkey Kong Country - Aquatic Ambience [Restored].mp3"))
audio_manager.load("firewall_fighter_music", os.path.join(assets_folder, "Donkey Kong Country 2 Soundtrack_ Bramble Blast.mp3"))
audio_manager.load("pass_the_password_music", os.path.join(assets_folder, "Zora's Domain - Day (The Legend of Zelda_ Breath of the Wild OST).mp3"))
audio_manager.load("packing_packets_music", os.path.join(assets_folder, "Original Tetris theme (Tetris Soundtrack).mp3"))
audio_manager.load("color_match_music", os.path.join(assets_folder, "Hateno Village (The Legend of Zelda_ Breath of the Wild OST).mp3"))

# Start playing the background music for the menu
# pygame.mixer.music.load(os.path.join(assets_folder, "Goblins_Dance_(Battle).wav"))
# pygame.mixer.music.play(-1)  # Loop indefinitely

# Start the initial scene
scene_manager.start_scene("Choice Scene")

# Set up the game clock for consistent frame rate
clock = pygame.time.Clock()
dt = 0

# Main game loop
while game_state.update():
    # Handle events, update the scene, and draw everything on the screen
    scene_manager.handle_events(dt)
    scene_manager.update(camera, screen, dt)
    scene_manager.draw(screen)
    pygame.display.flip()

    # Maintain a 60 FPS frame rate
    dt = clock.tick(60) / 1000

# Quit Pygame once the main loop ends
pygame.quit()