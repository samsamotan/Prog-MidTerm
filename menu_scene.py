from game_components.generic import interactable_objects
from game_components.generic import scene

menu_scene_objects = [
    interactable_objects.InteractableObject("game_components/assets/new_game.png", 270, 48, 225, 150, False),
    interactable_objects.InteractableObject("game_components/assets/load_game.png", 270, 48, 225, 210, False),
    interactable_objects.InteractableObject("game_components/assets/save_game.png", 270, 48, 225, 270, False)
]

menu_scene = scene.Scene('maps/black.jpg', menu_scene_objects)