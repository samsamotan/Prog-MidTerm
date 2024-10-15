import pygame as pg

class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pg.image.load(filename).convert()
        except pg.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)
    
    def image_at(self, rectangle):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        return image
    
    def images_at(self, rects):
        return [self.image_at(rect) for rect in rects]
    
    def load_strip(self, rect, image_count):
        tups=[(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups)