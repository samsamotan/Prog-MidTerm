import pygame as pg
from game_components.generic import camera
from game_components.generic import character
import pandas as pd

# pg setup
pg.init()
screen = pg.display.set_mode((1024, 576))
pg.display.set_caption("dootdoot")
clock = pg.time.Clock()
running = True
dt = 0
player = character.Player(15, 20, screen.get_width() / 2, screen.get_height() / 2)
pov = camera.Camera()
import scenes

scenes = {"pacman": scenes.pacman_scene, "menu": scenes.menu_scene, "first": scenes.first_scene}
#active_scene = menu_scene.menu_scene
active_scene = "pacman"
new_scene = active_scene

while running:

    # event handler
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # get keys getting pressed
    keys = pg.key.get_pressed()
    # changes player position
    player.move(keys, dt, scenes[active_scene])

    for object in scenes[active_scene].get_objects():
        try:
            check = object.interaction_check(keys, player)
            if check != None:
                new_scene = check
        except:
            pass

    if active_scene != new_scene:
        active_scene = new_scene
        
    # changes camera offset such that player stays in center
    pov.update(player, screen, scenes[active_scene])

    # loads all objects
    scenes[active_scene].render(screen, pov, player)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit()