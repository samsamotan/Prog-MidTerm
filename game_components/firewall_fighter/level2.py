import pygame as pg
import random


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
HEALTH_MAX = 3  # Maximum health (3 hearts)
score = 0

# Load images
background_image = pg.image.load("Mini Pixel Pack 3/SPACE BG.png").convert()
player_image = pg.image.load("Mini Pixel Pack 3/Player_ship (16 x 16).png").convert_alpha()
virus_image = pg.image.load("Mini Pixel Pack 3/Alan (16 x 16).png").convert_alpha()
safe_program_image = pg.image.load("Mini Pixel Pack 3/Bon_Bon (16 x 16).png").convert_alpha()
bullet_image = pg.image.load("Mini Pixel Pack 3/Player_charged_beam (16 x 16).png").convert_alpha()
number_font_image = pg.image.load("Mini Pixel Pack 3/Number_font (8 x 8).png").convert_alpha()
start_image = pg.image.load("Mini Pixel Pack 3/START (48 x 8).png").convert_alpha()
game_over_image = pg.image.load("Mini Pixel Pack 3/GAME_OVER (72 x 8).png").convert_alpha()

# Player class definition
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
        self.health = HEALTH_MAX  # Initialize health

    def move(self, keys):
        if keys[pg.K_a] and self.rect.left > 0:  # Left with 'A'
            self.rect.x -= 5
        if keys[pg.K_d] and self.rect.right < SCREEN_WIDTH:  # Right with 'D'
            self.rect.x += 5

# Threat class definition (Viruses and Safe Programs)
class Threat(pg.sprite.Sprite):
    def __init__(self, is_virus=True):
        super().__init__()
        self.image = virus_image if is_virus else safe_program_image
        self.rect = self.image.get_rect(center=(random.randint(30, SCREEN_WIDTH - 30), -30))
        self.is_virus = is_virus

    def update(self):
        self.rect.y += 2  # Slower fall speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove if it goes off screen

# Bullet class definition
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
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
    while True:
        screen.fill((0, 0, 0))  
        screen.blit(start_image, (SCREEN_WIDTH // 2 - start_image.get_width() // 2, SCREEN_HEIGHT // 4))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  
                    return

        pg.display.flip()

def draw_health(health):
    for i in range(health):
        pg.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH - (10 + i * 40), 10, 30, 30)) # Draw hearts as red squares

def draw_score(score):
    score_str = str(score)
    for i, digit in enumerate(score_str):
        digit_surface = number_font_image.subsurface(int(digit) * 8, 0, 8, 8)
        screen.blit(digit_surface, (10 + i * 10, 10)) # Adjust position as needed

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

        # Randomly spawn threats with reduced frequency
        if random.randint(1, 60) == 1:  
            is_virus = random.choice([True, False])
            new_threat = Threat(is_virus)
            all_sprites.add(new_threat)
            threats.add(new_threat)

        # Update all sprites
        all_sprites.update()

        # Check for collisions between bullets and threats
        hits_bullets = pg.sprite.groupcollide(bullets, threats, True, True)
        for threat_list in hits_bullets.values():
            for threat in threat_list:
                if threat.is_virus:
                    score += 1   # Increase score for hitting viruses
                else:           # If it's a safe program
                    player.health -= 1   # Decrease health for hitting safe programs

        # Check for collisions between player and threats (safe programs)
        hits_player = pg.sprite.spritecollide(player, threats, False)
        for hit in hits_player:
            if not hit.is_virus:   # Only decrease health on safe program collision
                player.health -= 1
                hit.kill()          # Remove the safe program after collision

                if player.health <= 0:   # End game if health reaches zero
                    print("Game Over!")
                    running = False
        
        # Level up condition
        if score >= POINTS_TO_LEVEL_UP:
            print("Level Up!")
            score = 0

        # Draw everything
        screen.blit(background_image, (0, 0))   # Draw the background image first
        all_sprites.draw(screen)
        
        draw_health(player.health)   # Draw player's health as hearts
        draw_score(score)             # Draw the score at the top left corner

        pg.display.flip()
        
        clock.tick(60)   # FPS
    
    return running

def show_game_over():
    while True:
        screen.fill((0, 0, 0))
        
        screen.blit(game_over_image,
                    (SCREEN_WIDTH // 2 - game_over_image.get_width() // 2,
                     SCREEN_HEIGHT // 4))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  
                    return

        pg.display.flip()

# Main program loop
while True:
    show_menu()
    game_active = game_loop()
    
    if not game_active: 
        show_game_over()

pg.quit()