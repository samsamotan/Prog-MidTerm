import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int = None, height: int = None, image = None):
        super().__init__()
        self.x = x
        self.y = y
        if image == None: # make transparent surface if no image provided
            self.image = pygame.Surface((width, height))
            self.image.fill((255,255,255))
            self.image.set_alpha(70)
        elif isinstance(image, str): # load image if filepath provided
            self.image = pygame.image.load(image)
        else: # use as image if surface provided
            self.image = image
        # set rect
        self.rect = self.image.get_rect(topleft = (x, y))
