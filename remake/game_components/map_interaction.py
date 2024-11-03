import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Map with Sprite")

map_background = pygame.image.load("remake/assets/map1.png")
map_background = pygame.transform.scale(map_background, (screen_width, screen_height))

# interactive areas
interaction_zones = {
    "red_house": pygame.Rect(22, 248, 100, 100),
    "green_house": pygame.Rect(550, 230, 80, 100),
    "red2_house": pygame.Rect(550, 350, 80, 100),
    "green2_house": pygame.Rect(698, 375, 78, 93),
    "blue2_house": pygame.Rect(698, 230, 78, 93),
    "blue_house": pygame.Rect(110, 2, 150, 50),
    "bridge2": pygame.Rect(108, 400, 37, 155),
    "bridge": pygame.Rect(240, 320, 70, 50),
}

# blocked zones
blocked_zones = [
    pygame.Rect(120, 260, 190, 60),
    pygame.Rect(0, 200, 270, 60),
    pygame.Rect(550, 0, 90, 290),
    pygame.Rect(690, 0, 120, 290),
    pygame.Rect(0, 0, 70, 150),
    pygame.Rect(0, 0, 350, 50),
    pygame.Rect(60, 140, 85, 20),
    pygame.Rect(180, 140, 400, 20),
    pygame.Rect(490, 0, 50, 120),
    pygame.Rect(330, 0, 120, 90),
    pygame.Rect(160, 300, 60, 75),
    pygame.Rect(240, 370, 90, 200),
    pygame.Rect(460, 370, 90, 200),
    pygame.Rect(470, 280, 80, 80),
    pygame.Rect(290, 420, 200, 100),
    pygame.Rect(145, 490, 100, 50),
    pygame.Rect(145, 440, 20, 50),
    pygame.Rect(0, 440, 110, 100),
    pygame.Rect(0, 500, 70, 100),
    pygame.Rect(0, 200, 20, 250),
    pygame.Rect(190, 500, 70, 100),
    pygame.Rect(780, 200, 20, 400),
    pygame.Rect(710, 530, 70, 60),
    pygame.Rect(550, 530, 70, 60),
    pygame.Rect(550, 590, 200, 20),
]

# Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 30))  # Placeholder for player sprite
        self.image.fill((0, 128, 255))         # color for the player
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self, keys_pressed):
        # Horizontal movement
        original_x = self.rect.x
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Check for horizontal collisions
        for zone in blocked_zones:
            if self.rect.colliderect(zone):
                self.rect.x = original_x

        # Vertical movement
        original_y = self.rect.y
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Check for vertical collisions
        for zone in blocked_zones:
            if self.rect.colliderect(zone):
                self.rect.y = original_y


player = Player(100, 100)  # Starting position
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Update player movement
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)

    # Check for interactions with different zones
    if player.rect.colliderect(interaction_zones["red_house"]):
        print("You are near the red house!")
    elif player.rect.colliderect(interaction_zones["green_house"]):
        print("You are near the green house!")
    elif player.rect.colliderect(interaction_zones["red2_house"]):
        print("You are near the red house!")
    elif player.rect.colliderect(interaction_zones["bridge"]):
        print("You are on the bridge!")

    screen.blit(map_background, (0, 0))  # Draw the map background
    all_sprites.draw(screen)             # Draw the player

#### BOX GUIDE! shows the boxes for interactive (red) and blocked (blue) areas
### delete when the game is final this should be for cleaning the game 
    # Draw interaction and blocked zones for visualization (optional)
    for name, rect in interaction_zones.items():
        pygame.draw.rect(screen, (255, 0, 0), rect, 2)  # Interaction zones in red

    for rect in blocked_zones:
        pygame.draw.rect(screen, (0, 0, 255), rect, 2)  # Blocked zones in blue for visibility
### DELETE 9 LINES IF U DONT WANT TO SEE THE BOXES (FROM LINE 119 TO 127)

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Control the frame rate