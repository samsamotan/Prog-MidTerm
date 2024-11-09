import pygame
from ..objects import *
from ..firewall_fighter import *
from ..scene import Scene
import os
import random

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

# Game constants
POINTS_TO_LEVEL_UP = 30
HEALTH_MAX = 3

base_path = "Mini Pixel Pack 3"

background_image = os.path.join(assets_folder, base_path, "SPACE BG.png")
player_image = os.path.join(assets_folder, base_path, "Player ship", "Player_ship (16 x 16).png")
virus_image = os.path.join(assets_folder, base_path, "Enemies", "Alan (16 x 16).png")
safe_program_image = os.path.join(assets_folder, base_path, "Enemies", "Bon_Bon (16 x 16).png")
bullet_image = os.path.join(assets_folder, base_path, "Projectiles", "Player_charged_beam (16 x 16).png")
number_font_image = os.path.join(assets_folder, base_path, "UI objects", "Number_font (8 x 8).png")
start_image = os.path.join(assets_folder, base_path, "UI objects", "START (48 x 8).png")
game_over_image = os.path.join(assets_folder, base_path, "UI objects", "GAME_OVER (72 x 8).png")


class FirewallFighter(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)  


    def start(self):
        self.player = Player(512, 526, 15, 20)
        self.health_bar = HealthBar(HEALTH_MAX, self.width)
        self.score_counter = ScoreCounter(10, 10)
        self.threats = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.all_sprites.add(self.score_counter, self.health_bar)

    def handle_events(self, dt):
        for event in self.game_state.get_events():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    bullet = Bullet(self.player.rect.centerx, self.player.rect.top, bullet_image)
                    self.all_sprites.add(bullet)
                    self.bullets.add(bullet)
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self, vertical_movement = False)   

    def update_score(self, amount):
        """Update the score by a specified amount and refresh the display."""
        self.score += amount
        self.image = self.font.render(f"Score: {self.score}", True, self.color)

    def set_score(self, new_score):
        """Set the score to a specific value and refresh the display."""
        self.score = new_score
        self.image = self.font.render(f"Score: {self.score}", True, self.color)

    def reset_score(self):
        """Reset the score to zero and refresh the display."""
        self.score = 0
        self.image = self.font.render(f"Score: {self.score}", True, self.color)

    def update(self, dt):
         # Randomly spawn threats with reduced frequency
        if random.randint(1, 60) == 1:  
            is_virus = random.choice([True, False])
            new_threat = Threat(virus_image,  safe_program_image, is_virus)
            self.all_sprites.add(new_threat)
            self.threats.add(new_threat)
            
        # Update all sprites
        self.all_sprites.update()

        # Check for collisions between bullets and threats
        hits_bullets = pygame.sprite.groupcollide(self.bullets, self.threats, True, True)
        for threat_list in hits_bullets.values():
            for threat in threat_list:
                if threat.is_virus():
                    self.score_counter.update_score(1)   # Increase score for hitting viruses
                else:           # If it's a safe program
                    self.health_bar.update_health(1)  # Decrease health for hitting safe programs

        # Check for collisions between player and threats (safe programs)
        hits_player = pygame.sprite.spritecollide(self.player, self.threats, True)
        for hit in hits_player:
            if not hit.is_virus():   # Only decrease health on safe program collision
                self.health_bar.update_health(1)
                hit.kill()          # Remove the safe program after collision

        if self.health_bar.get_current_health() <= 0:   # End game if health reaches zero
            print("Game Over!")
            self.scene_manager.quit_scene("Firewall Fighter", "Main Scene")

    def draw(self, screen, camera):
        screen.fill((0,0,0))
        self.all_sprites.draw(screen) 
        screen.blit(self.player.image, self.player.rect)