import pygame
from ..objects import *
from ..firewall_fighter import *
from ..scene import Scene
import os
import random

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

# Game constants
POINTS_TO_LEVEL_UP = 15
HEALTH_MAX = 3

base_path = "Mini Pixel Pack 3"

background_image = os.path.join(assets_folder, base_path, "SPACE BG.png")
player_image = os.path.join(assets_folder, base_path, "Player ship", "Player_ship (16 x 16).png")
virus_image = os.path.join(assets_folder, "red viruses.png")
safe_program_image = os.path.join(assets_folder,"safe program.png")
bullet_image = os.path.join(assets_folder, base_path, "Projectiles", "Player_charged_beam (16 x 16).png")
number_font_image = os.path.join(assets_folder, base_path, "UI objects", "Number_font (8 x 8).png")
start_image = os.path.join(assets_folder, base_path, "UI objects", "START (48 x 8).png")
game_over_image = os.path.join(assets_folder, base_path, "UI objects", "GAME_OVER (72 x 8).png")

class FirewallFighter(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)
        pygame.mixer.init()  # Initialize pygame mixer

    def start(self):
        # Play background music
        self.background_music = pygame.mixer.music.load(os.path.join(assets_folder, "Donkey Kong Country 2 Soundtrack_ Bramble Blast.mp3"))
        pygame.mixer.music.play(-1)  # Loop the background music

        self.background = pygame.image.load(os.path.join(assets_folder,"space_invaders.png"))
        self.player = Player(512, 526, 15, 20, os.path.join(assets_folder, "spaceship.png"))
        self.health_bar = HealthBar(HEALTH_MAX, self.width, os.path.join(assets_folder, "heart.png"))
        self.score_counter = ScoreCounter(10, 10)
        self.threats = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.all_sprites.add(self.score_counter, self.health_bar)

    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    bullet = Bullet(self.player.rect.centerx, self.player.rect.top, bullet_image)
                    self.all_sprites.add(bullet)
                    self.bullets.add(bullet)
                    self.shoot_sound = pygame.mixer.Sound(os.path.join(assets_folder, "laser.wav"))
                    self.shoot_sound.play()

        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self, vertical_movement=False)

    def update(self, dt):
        # Randomly spawn threats with reduced frequency
        if random.randint(1, 60) == 1:  
            is_virus = random.choice([True, False])
            new_threat = Threat(virus_image, safe_program_image, is_virus)
            self.all_sprites.add(new_threat)
            self.threats.add(new_threat)

        # Check for collisions between bullets and threats
        hits_bullets = pygame.sprite.groupcollide(self.bullets, self.threats, True, True)
        for threat_list in hits_bullets.values():
            for threat in threat_list:
                if threat.is_virus():
                    self.score_counter.update_score(1)   # Increase score for hitting viruses
                else:           # If it's a safe program
                    self.health_bar.update_health(1)  # Decrease health for hitting safe programs
                    self.shoot_sound.play()

        # Check for collisions between player and threats (safe programs)
        hits_player = pygame.sprite.spritecollide(self.player, self.threats, True)
        for hit in hits_player:
            if not hit.is_virus():   # Only decrease health on safe program collision
                self.health_bar.update_health(1)
                hit.kill()          # Remove the safe program after collision
                self.shoot_sound.play()

        # Update all sprites
        self.all_sprites.update()

        # Check if the player has reached the level-up score
        if self.score_counter.score >= POINTS_TO_LEVEL_UP:
            self.scene_manager.start_scene("Main Scene")
        
        # Only transition to game over if health reaches zero
        if self.health_bar.get_current_health() <= 0:   # End game if health reaches zero
            print("Game Over!")
            self.scene_manager.start_scene("Game Over Scene")

    def draw(self, screen):
        screen.blit(self.background, (0, 0, 1024, 576))
        self.all_sprites.draw(screen) 
        screen.blit(self.player.image, self.player.rect)

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, max_health, screen_width, heart_image_path):
        super().__init__()
        self.max_health = max_health
        self.current_health = max_health
        self.screen_width = screen_width

        # Load and scale the heart image
        self.heart_image = pygame.image.load(heart_image_path)
        self.heart_image = pygame.transform.scale(self.heart_image, (20, 20))  # Scale the heart image to a smaller size
        self.heart_spacing = 5  # Spacing between hearts
        self.image = pygame.Surface((self.max_health * (self.heart_image.get_width() + self.heart_spacing), 
                                     self.heart_image.get_height()), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topright=(self.screen_width - 10, 10))  # Position at top-right corner of the screen

    def update_health(self, amount):
        """Adjust health by amount; decrease if amount is positive, increase if negative."""
        self.current_health = max(0, min(self.max_health, self.current_health - amount))

    def update(self):
        """Redraw hearts based on current health."""
        self.image.fill((0, 0, 0, 0))  # Clear the surface with transparency
        for i in range(self.current_health):
            x = i * (self.heart_image.get_width() + self.heart_spacing)
            self.image.blit(self.heart_image, (x, 0))

    def get_current_health(self):
        return self.current_health

    def draw(self, screen):
        """Draws hearts on the screen representing the current health."""
        for i in range(self.current_health):
            x = self.heart_spacing + (i * (self.heart_image.get_width() + self.heart_spacing))  # Space out hearts
            y = self.heart_spacing  # Position hearts at the top of the screen
            screen.blit(self.heart_image, (x, y))
