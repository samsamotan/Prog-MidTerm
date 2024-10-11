# Example file showing a circle moving on screen
import pygame
import Character, Actions, Camera, Zones
# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption("dootdoot")
clock = pygame.time.Clock()
running = True
dt = 0
player = Character.character(screen.get_width() / 2, screen.get_height() / 2)

map_image = pygame.image.load('maps\map_image.webp')
map_width, map_height = map_image.get_size()

camera = Camera.Camera()

firstZone = Zones.Zone('maps\map_image.webp')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    Actions.move(player, keys, dt)

    camera.update(player, screen, camera, firstZone)

    firstZone.render(screen, camera, player)
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()