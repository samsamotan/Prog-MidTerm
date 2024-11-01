import pygame as pg
from game_components.scene_manager import SceneManager
from game_components.scenes import *

pg.init()
screen = pg.display.set_mode((1024, 576))
pg.display.set_caption("Computer Conquest")

running = True
dt = 0

scene_manager = SceneManager("Main Menu")
scene_manager.add_scene("Main Menu", MainMenu)
scene_manager.add_scene("Main Scene", MainScene)


scene_manager.start_scene("Main Menu")

clock = pg.time.Clock()

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        
    keys = pg.key.get_pressed()

    scene_manager.handle_events(events, keys, dt)
    scene_manager.update

    scene_manager.draw(screen)
    pg.display.flip()
    dt = clock.tick(24) / 1000

pg.quit()