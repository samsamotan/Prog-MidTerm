# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption("Enter Game Name")
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = [screen.get_width() / 2, screen.get_height() / 2]
player_speed = 300

map_image = pygame.image.load('map_image.webp')
map_width, map_height = map_image.get_size()

camera_x = 0
camera_y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos[1] >= 0:
            player_pos[1] -= player_speed * dt
    if keys[pygame.K_s]:
        if player_pos[1] <= map_height - 30:
            player_pos[1] += player_speed * dt
    if keys[pygame.K_a]:
        if player_pos[0] >= 0:
            player_pos[0] -= player_speed * dt
    if keys[pygame.K_d]:
        if player_pos[0] <= map_width - 20:
            player_pos[0] += player_speed * dt
    print(player_pos[1],map_height)
    if player_pos[0] < screen.get_width() // 2:
        camera_x = 0
    elif player_pos[0] > map_width - screen.get_width() // 2:
        camera_x = map_width - screen.get_width()
    else:
        camera_x = player_pos[0] - screen.get_width() // 2

    if player_pos[1] < screen.get_height() // 2:
        camera_y = 0
    elif player_pos[1] > map_height - screen.get_height() // 2:
        camera_y = map_height - screen.get_height()
    else:
        camera_y = player_pos[1] - screen.get_height() // 2   

    screen.fill((255, 255, 255))

    screen.blit(map_image, (-camera_x, -camera_y))

    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0] - camera_x, player_pos[1] - camera_y, 20, 30))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()