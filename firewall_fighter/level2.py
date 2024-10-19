import pygame as pg
import random
import character

# Initialize Pygame
pg.init()

# Screen dimensions and setup
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 360
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Firewall Fighter: Virus Hunt Zone")
clock = pg.time.Clock()

# Game constants
POINTS_TO_LEVEL_UP = 30
score = 0

# Player class definition
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 30))
        self.image.fill((0, 255, 0))  # Green player
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))

    def move(self, keys):
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pg.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

# Threat class definition (Viruses and Safe Programs)
class Threat(pg.sprite.Sprite):
    def __init__(self, is_virus=True):
        super().__init__()
        self.image = pg.Surface((30, 30))
        self.image.fill((255, 0, 0) if is_virus else (255, 255, 255))  # Red for viruses, white for safe programs
        self.rect = self.image.get_rect(center=(random.randint(30, SCREEN_WIDTH - 30), -30))

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove if it goes off screen

# Bullet class definition
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill((255, 255, 0))  # Yellow bullets
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()  # Remove if it goes off screen

# Create sprite groups
all_sprites = pg.sprite.Group()
threats = pg.sprite.Group()
bullets = pg.sprite.Group()

def show_menu():
    font = pg.font.Font(None, 74)
    title_surface = font.render("Firewall Fighter", True, (255, 255, 255))
    start_surface = font.render("Press Enter to Start", True, (255, 255, 255))
    
    while True:
        screen.fill((0, 0, 0))  
        screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(start_surface, (SCREEN_WIDTH // 2 - start_surface.get_width() // 2, SCREEN_HEIGHT // 2))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  
                    return

        pg.display.flip()

def game_loop():
    global score
    score = 0
    
    player = Player()
    all_sprites.add(player)

    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:  
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        keys = pg.key.get_pressed()
        player.move(keys)

        # Randomly spawn threats
        if random.randint(1, 20) == 1:  
            is_virus = random.choice([True, False])
            new_threat = Threat(is_virus)
            all_sprites.add(new_threat)
            threats.add(new_threat)

        # Update all sprites
        all_sprites.update()

        # Check for collisions between bullets and threats
        hits = pg.sprite.groupcollide(bullets, threats, True, True)
        for hit in hits:
            score += 1

        # Level up condition
        if score >= POINTS_TO_LEVEL_UP:
            print("Level Up!")
            score = 0

        # Draw everything
        screen.fill((0, 0, 0))  
        all_sprites.draw(screen)

        font = pg.font.Font(None, 36)
        text_surface = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        pg.display.flip()
        
        clock.tick(60)  

# Main program loop
while True:
    show_menu()
    game_loop()

pg.quit()