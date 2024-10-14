import scene_object
import pygame
import scenes.first_scene as first_scene

class InteractableObject(scene_object.SceneObject):
    def __init__(self, *args, interaction = True, interactions = {pygame.K_e: first_scene.first_scene}):
        super().__init__(*args)
        self.interaction = interaction
        self.interactions = interactions
    def interaction_check(self, keys, player):
        for interaction in list(self.interactions.keys()):
            if keys[interaction] and super().within(player.get_x_pos(), player.get_y_pos()):
                return self.interactions[interaction]