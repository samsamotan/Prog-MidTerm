from game_components.generic import scene_object
import pygame as pg
from .within import within

class InteractableObject(scene_object.SceneObject):
    def __init__(self, *args, interaction = True, interactions):
        super().__init__(*args)
        self.interaction = interaction
        self.interactions = interactions
    def interaction_check(self, keys, player):
        for interaction in list(self.interactions.keys()):
            if keys[interaction] and within(self.hitbox, player.get_x_pos(), player.get_y_pos()):
                return self.interactions[interaction]
            elif keys[interaction] and within(self.hitbox, player.get_x_pos()+player.get_x_size(), player.get_y_pos()+player.get_y_size()):
                return self.interactions[interaction]
            elif keys[interaction] and within(self.hitbox, player.get_x_pos(), player.get_y_pos()+player.get_y_size()):
                return self.interactions[interaction]
            elif keys[interaction] and within(self.hitbox, player.get_x_pos()+player.get_x_size(), player.get_y_pos()):
                return self.interactions[interaction]