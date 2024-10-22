from game_components.generic import scene
from game_components.generic import scene_object
from game_components.generic import interactable_objects
from game_components.pacman import pacman_map
from game_components.pacman import pacman_scene
import pygame as pg

first_scene_objects = [
    scene_object.SceneObject("game_components/assets/tree.webp", 238, 280, 100, 100, True),
    scene_object.SceneObject("game_components/assets/tree.webp", 238, 280, 500, 500, True),
    interactable_objects.InteractableObject("game_components/assets/pixil-frame-0.png", 50, 30, 690, 220, False, interactions = {pg.K_e: "pacman"})
    ]
first_scene = scene.Scene(False,'maps/black.jpg', first_scene_objects)

menu_scene_objects = [
    interactable_objects.InteractableObject("game_components/assets/new_game.png", 270, 48, 225, 150, False, interactions = {pg.K_e: "first"}),
    interactable_objects.InteractableObject("game_components/assets/load_game.png", 270, 48, 225, 210, False, interactions = {pg.K_e: "first"}),
    interactable_objects.InteractableObject("game_components/assets/save_game.png", 270, 48, 225, 270, False, interactions = {pg.K_e: "first"})
]

menu_scene = scene.Scene(False, 'maps/black.jpg', menu_scene_objects)

pacman_scene_objects = [
    interactable_objects.InteractableObject("game_components/assets/pixil-frame-0.png", 50, 30, 1024/2+20, 512/2+20, False, interactions = {pg.K_e: "menu"})
]

pacman_scene = pacman_scene.PacmanScene(True, pacman_map.PacmanMap('game_components/assets/edge_spritesheet size 2.png', ["left_cap", "top_cap", "bottom_cap", "right_cap", "left_bottom_corner", "left_top_corner", "right_top_corner", "right_bottom_corner", "topless_threeway", "bottomless_threeway", "rightless_threeway", "leftless_threeway", "fourway", "horizontal", "vertical", "blank"]), pacman_scene_objects, 1024, 576)




