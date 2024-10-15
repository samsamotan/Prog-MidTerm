import pygame as pg
import map

pg.init()
screen = pg.display.set_mode((960, 540))
pg.display.set_caption("dootdoot")
clock = pg.time.Clock()
running = True

scene = map.PacmanMap('pacman minigame/assets/edge_spritesheet.png', ["left_cap", "top_cap", "bottom_cap", "right_cap", "left_bottom_corner", "left_top_corner", "right_top_corner", "right_bottom_corner", "topless_threeway", "bottomless_threeway", "rightless_threeway", "leftless_threeway", "fourway", "horizontal", "vertical"])

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    scene.render(screen)
    pg.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit()