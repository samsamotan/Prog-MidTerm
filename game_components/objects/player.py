import pygame
from .game_object import GameObject

class Player(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None, speed = 300):
        super().__init__(x, y, width, height, image)
        self.speed = speed
        self.velocity = pygame.Vector2(0, 0)

    def get_pos(self):
        return (self.rect.x, self.rect.y)
    
    def set_pos(self, pos):
        self.rect = self.image.get_rect(topleft = pos)
    
    def move(self, keys, dt, scene, *groups, vertical_movement = True, horizontal_movement = True):
        # get velocity
        self.velocity.x = (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed * dt
        self.velocity.y = (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed * dt

        #Horizontal movement
        if horizontal_movement:
            self.rect.x += self.velocity.x
            for group in groups:
                for obstacle in group:
                    if self.rect.colliderect(obstacle.rect):
                        if self.velocity.x > 0:  # Moving right
                            self.rect.right = obstacle.rect.left
                        elif self.velocity.x < 0:  # Moving left
                            self.rect.left = obstacle.rect.right

        # Vertical movement
        if vertical_movement:
            self.rect.y += self.velocity.y
            for group in groups:
                for obstacle in group:
                    if self.rect.colliderect(obstacle.rect):
                        if self.velocity.y > 0:  # Moving down
                            self.rect.bottom = obstacle.rect.top
                        elif self.velocity.y < 0:  # Moving up
                            self.rect.top = obstacle.rect.bottom

        # Don't move if at border
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > scene.get_width() - self.rect.width:
            self.rect.x = scene.get_width() - self.rect.width
        if self.rect.y > scene.get_height() - self.rect.height:
            self.rect.y = scene.get_height() - self.rect.height

class BigPlayer(Player):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None, speed = 300):
        enlarged = pygame.transform.scale_by(pygame.image.load(image), 2)
        super().__init__(x, y, width, height, enlarged)
        self.speed = speed
        self.velocity = pygame.Vector2(0, 0)