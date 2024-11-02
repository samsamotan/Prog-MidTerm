import pygame as pg

class GameState:
    def __init__(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.keys = pg.key.get_pressed()
        self.events = pg.event.get()

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.keys = pg.key.get_pressed()
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                return False
        return True
    
    def get_mouse_pos(self):
        return self.mouse_pos
    
    def get_keys(self):
        return self.keys
    
    def get_events(self):
        return self.events