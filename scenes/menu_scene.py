import interactable_objects
import scene

menu_scene_objects = [
    interactable_objects.InteractableObject("tree.webp", 238, 280, 180, 360, False)
]

menu_scene = scene.Scene('maps/map_image.webp', menu_scene_objects)