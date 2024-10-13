# Example file showing a circle moving on screen
import pygame
import character, camera, zones
# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption("dootdoot")
clock = pygame.time.Clock()
running = True
dt = 0
player = character.Player(20, 30, screen.get_width() / 2, screen.get_height() / 2)

pov = camera.Camera()

firstZone = zones.Zone('maps\map_image.webp')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get keys getting pressed
    keys = pygame.key.get_pressed()
    # changes player position
    player.move(keys, dt, firstZone)

    # changes camera offset such that player stays in center
    pov.update(player, screen, firstZone)

    # loads all objects
    firstZone.render(screen, pov, player)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()