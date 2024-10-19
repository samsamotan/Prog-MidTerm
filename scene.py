import pygame
import scene_object
class Scene():
    def __init__(self, image, objects):
        self.map_image = pygame.image.load(image)
        self.map_width, self.map_height = self.map_image.get_size()
        self.scene_objects = objects
    def get_height(self):
        return self.map_height
    def get_width(self):
        return self.map_width
    def get_objects(self):
        return self.scene_objects
    def render(self, screen, camera, player):
        # background
        screen.fill((255, 255, 255))
        screen.blit(self.map_image, (-camera.get_x_pos(), -camera.get_y_pos()))
 
        # objects
        for object in self.scene_objects:
            screen.blit(object.get_image(), (object.get_x_pos() - camera.get_x_pos(), object.get_y_pos() - camera.get_y_pos()))

        # player
        pygame.draw.rect(screen, (255, 0, 0), (player.get_x_pos() - camera.get_x_pos(), player.get_y_pos() - camera.get_y_pos(), player.get_x_size(), player.get_y_size()))
       
        # flip() the display to put your work on screen
        pygame.display.flip()
