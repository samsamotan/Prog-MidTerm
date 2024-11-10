import pygame
from .game_object import GameObject

class InteractiveObject(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, scene_manager = None, current_scene = None, target_scene = None, image = None):
        super().__init__(x, y, width, height, image)
        self.actions = {}
        self.scene_manager = scene_manager
        self.current_scene = current_scene
        self.target_scene = target_scene

    def add_action(self, key, function):
        """Add an interaction to the object"""
        self.actions[key] = function

    def interact(self, events, player):
        if self.rect.colliderect(player.rect):
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key in self.actions:
                        if self.actions[event.key] == "change scene":
                            self.scene_manager.start_scene(self.target_scene)
                        if self.actions[event.key] == "new scene":
                            self.scene_manager.start_scene(self.target_scene)