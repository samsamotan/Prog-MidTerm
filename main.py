import pygame as pg
import camera
from firewall_fighter.character import *
import pandas as pd
import scenes.menu_scene as menu_scene

# pg setup
pg.init()
screen = pg.display.set_mode((720, 360))
pg.display.set_caption("dootdoot")
clock = pg.time.Clock()
running = True
dt = 0
player = Player(20, 30, screen.get_width() / 2, screen.get_height() / 2)

pov = camera.Camera()

active_scene = menu_scene.menu_scene
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
    player.move(keys, dt, active_scene)

    
    for object in active_scene.get_objects():
        try:
            check = object.interaction_check(keys, player)
            print(check)
            if check != None:
                new_scene = check
        except:
            pass

    if active_scene != new_scene:
        active_scene = new_scene
        
    # changes camera offset such that player stays in center
    pov.update(player, screen, active_scene)

    # loads all objects
    active_scene.render(screen, pov, player)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit()