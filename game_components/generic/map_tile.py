import sys
from pathlib import Path
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)

from game_components.generic import scene_object
class MapTile(scene_object.SceneObject):
    def __init__(self, image, x, y, obstacle):
        super().__init__(None,32,32,x,y,obstacle)
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