import pygame

class GameState:
    def __init__(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()
        self.events = pygame.event.get()

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                return False
        return True
    
    def get_mouse_pos(self):
        return self.mouse_pos
    
    def get_keys(self):
        return self.keys
    
    def get_events(self):
        return self.events
    
    def save_game(self):
        pass

    def load_game(self):
        pass