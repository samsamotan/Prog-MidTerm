import pygame
from game_components.scene_manager import SceneManager
from game_components.game_state import GameState
from game_components.audio_manager import AudioManager
from game_components.scenes import *
from game_components.objects.camera import Camera

pygame.init()
print(pygame.display.list_modes())
screen = pygame.display.set_mode((1024,576))

pygame.display.set_caption("Computer Conquest")

running = True
dt = 0

camera = Camera(screen)
game_state = GameState()
audio_manager = AudioManager()
scene_manager = SceneManager(game_state, audio_manager)
scene_manager.add_scene("Start Scene", StartScreen)
scene_manager.add_scene("Main Scene", MainScene)
scene_manager.add_scene("Opening Scene", Opening)

#Kenneth's Minigame
scene_manager.add_scene("Virus Vacuum", VirusVacuum)

#Kath's Minigame
scene_manager.add_scene("Firewall Fighter", FirewallFighter)

#Faith's Minigame
scene_manager.add_scene("Pass the Password", PassThePassword)

#Ari's Minigame
scene_manager.add_scene("Packing Packets", PackingPackets)

#Franco's Minigame
scene_manager.add_scene("Color Match", ColorMatch)

scene_manager.start_scene("Pass the Password")

clock = pygame.time.Clock()

while game_state.update():
    scene_manager.handle_events(dt)
    scene_manager.update(camera, screen, dt)

    scene_manager.draw(screen, camera)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()