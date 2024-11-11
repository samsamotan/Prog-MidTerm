import pygame

class GameState:
    def __init__(self, camera):
        self.keys = pygame.key.get_pressed()
        self.events = pygame.event.get()
        self.camera = camera
        self.passed = False
        self.colored = False
        self.player_pos = (875, 450)

    def update(self, offset_x, offset_y, scale_x, scale_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.mouse_pos = ((mouse_x - offset_x) / scale_x, (mouse_y - offset_y) / scale_y)
        self.keys = pygame.key.get_pressed()
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.save_game()
                return False
        return True
    
    def get_mouse_pos(self):
        return self.mouse_pos
    
    def get_keys(self):
        return self.keys
    
    def get_events(self):
        return self.events
    
    def save_game(self):
        values = [self.colored, self.passed, self.player_pos[0], self.player_pos[1]]

        # Save to a file
        with open("data.txt", "w") as file:
            for value in values:
                file.write(f"{value}\n")

    def load_game(self):
        with open("data.txt", "r") as file:
            values = [line for line in file]
        self.colored = values[0] == "True\n"
        self.passed = values[1] == "True\n"
        self.player_pos = (int(values[2]), int(values[3]))


    def add_popup(self, succeeded):
        self.popup = True
        self.succeeded = succeeded