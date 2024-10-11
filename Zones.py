import pygame
import zone_object
class Zone():
    def __init__(self, image):
        self.map_image = pygame.image.load(image)
        self.map_width, self.map_height = self.map_image.get_size()
        self.zone_objects = [zone_object.ZoneObject(20, 30, 100, 100, True)]
    def get_height(self):
        return self.map_height
    def get_width(self):
        return self.map_width
    def get_objects(self):
        return self.zone_objects
    def render(self, screen, camera, player):
        screen.fill((255, 255, 255))
        screen.blit(self.map_image, (-camera.get_x_pos(), -camera.get_y_pos()))

        pygame.draw.rect(screen, (255, 0, 0), (player.get_x_pos() - camera.get_x_pos(), player.get_y_pos() - camera.get_y_pos(), player.get_x_size(), player.get_y_size()))
        for object in self.zone_objects:
            pygame.draw.rect(screen, (0, 255, 0), (object.get_x_pos() - camera.get_x_pos(), object.get_y_pos() - camera.get_y_pos(), object.get_x_size(), object.get_y_size()))

        # flip() the display to put your work on screen
        pygame.display.flip()
