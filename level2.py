import pygame
import character
import camera
import pandas as pd
import scenes.menu_scene as menu_scene
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption("Firewall Fighter: Virus Hunt Zone")
clock = pygame.time.Clock()
running = True
dt = 0

# Initialize player and camera
player = character.Player(20, 30, screen.get_width() / 2, screen.get_height() / 2)
pov = camera.Camera()

# Game constants
POINTS_TO_LEVEL_UP = 30
score = 0

# Groups for sprites
all_sprites = pygame.sprite.Group()
threats = pygame.sprite.Group()
bullets = pygame.sprite.Group()

class Threat(pygame.sprite.Sprite):
    def __init__(self, is_virus=True):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0) if is_virus else (255, 255, 255))  # Red for viruses, white for safe programs
        self.rect = self.image.get_rect(center=(random.randint(30, screen.get_width() - 30), -30))

    def update(self):
        self.rect.y += 5
        if self.rect.top > screen.get_height():
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))  # Yellow bullets
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

active_scene = menu_scene.menu_scene
new_scene = active_scene

# Main game loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Shoot on spacebar press
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Get keys being pressed
    keys = pygame.key.get_pressed()
    player.move(keys, dt, active_scene)

    # Spawn threats randomly
    if random.randint(1, 20) == 1:  # Adjust frequency as needed
        is_virus = random.choice([True, False])
        new_threat = Threat(is_virus)
        all_sprites.add(new_threat)
        threats.add(new_threat)

    # Update all sprites
    all_sprites.update()

    # Check for collisions between bullets and threats
    hits = pygame.sprite.groupcollide(bullets, threats, True, True)
    for hit in hits:
        score += 1

    # Level up condition
    if score >= POINTS_TO_LEVEL_UP:
        print("Level Up!")
        score = 0

    # Render everything
    screen.fill((0, 0, 0))  # Clear screen with black background
    all_sprites.draw(screen)

    # Display score on screen (optional)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    # Update the camera and render active scene objects
    pov.update(player, screen, active_scene)

    pygame.display.flip()
    
    # Limit FPS to 60 and calculate delta time
    dt = clock.tick(60) / 1000

pygame.quit()
