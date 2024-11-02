import pygame as pg
from game_components.scene_manager import SceneManager
from game_components.game_state import GameState
from game_components.scenes import *
from game_components.objects.camera import Camera

pg.init()
screen = pg.display.set_mode((1024, 576))
pg.display.set_caption("Computer Conquest")

running = True
dt = 0

camera = Camera(screen)

game_state = GameState()
scene_manager = SceneManager(game_state)
scene_manager.add_scene("Main Menu", MainMenu)
scene_manager.add_scene("Main Scene", MainScene)
scene_manager.add_scene("Virus Vacuum", VirusVacuum)
scene_manager.add_scene("Firewall Fighter", FirewallFighter)


scene_manager.start_scene("Firewall Fighter")

clock = pg.time.Clock()

while game_state.update():
    scene_manager.handle_events(dt)
    scene_manager.update(camera, screen, dt)

    scene_manager.draw(screen, camera)
    pg.display.flip()
    dt = clock.tick(60) / 1000

pg.quit()