from game_components.generic import scene
from game_components.generic import scene_object
import pygame

first_scene_objects = [
    scene_object.SceneObject("game_components/assets/tree.webp", 238, 280, 100, 100, True),
    scene_object.SceneObject("game_components/assets/tree.webp", 238, 280, 500, 500, True),
    ]
first_scene = scene.Scene('maps/map_image.webp', first_scene_objects)








