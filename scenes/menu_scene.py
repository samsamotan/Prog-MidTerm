import interactable_objects
import scene

menu_scene_objects = [
    interactable_objects.InteractableObject("assets/new_game.png", 771, 161, 180, 360, False)
]

menu_scene = scene.Scene('maps/black.jpg', menu_scene_objects)