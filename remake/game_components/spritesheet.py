import pygame as pg

class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pg.image.load(filename).convert_alpha()

    def image_at(self, rectangle):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        return image
    
    def images_at(self, rects):
        return [self.image_at(rect) for rect in rects]
    
    def load_strip(self, rect, image_count):
        row=[(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(row)
    
    def collapse(self, grid):
        collapsed_grid = []
        for row in grid:
            for sprite in row:
                collapsed_grid.append(sprite)
        return collapsed_grid
    
    def load_grid(self, rect, column_count, row_count):
        grid=[(rect[0], rect[1]+rect[3]*x, rect[2], rect[3]) for x in range(row_count)]
        return self.collapse([self.load_strip(row, column_count) for row in grid])