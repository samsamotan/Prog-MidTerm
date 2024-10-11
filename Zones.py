import pygame
class Zone():
    def __init__(self, image):
        self.map_image = pygame.image.load(image)
        self.map_width, self.map_height = self.map_image.get_size()
    def getHeight(self):
        return self.map_width
    def getWidth(self):
        return self.map_height
    def render(self, screen, camera, player):
        screen.fill((255, 255, 255))
        screen.blit(self.map_image, (-camera.getXPos(), -camera.getYPos()))

        pygame.draw.rect(screen, (255, 0, 0), (player.getXPos() - camera.getXPos(), player.getYPos() - camera.getYPos(), 20, 30))

        # flip() the display to put your work on screen
        pygame.display.flip()
