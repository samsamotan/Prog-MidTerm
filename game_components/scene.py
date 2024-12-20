import pygame

class Scene:
    def __init__(self, scene_manager, game_state, audio_manager, width, height):
        self.scene_manager = scene_manager
        self.game_state = game_state
        self.audio_manager = audio_manager
        self.width = width
        self.height = height
        self.obstacles = pygame.sprite.Group()
        self.interactions = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def get_obstacle(self):
        return self.obstacles

    def start(self):
        pass

    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height