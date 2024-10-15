class MapTile():
    def __init__(self, image, x, y):
        self.image = image
        self.x, self.y = x, y
    def blitme(self, screen):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        screen.blit(self.image, self.rect)
    def get_x_pos(self):
        return self.x
    def get_y_pos(self):
        return self.y
    def get_image(self):
        return self.image