import pygame as pg

import pygame as pg

class SpriteSheet:
    def __init__(self, filename):
        """Load the sprite sheet from a file."""
        try:
            self.sheet = pg.image.load(filename).convert_alpha()  # Using convert_alpha for transparency
        except pg.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle):
        """Extract a single image from the sprite sheet given a rectangle."""
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size, pg.SRCALPHA).convert_alpha()  # Preserve transparency
        image.blit(self.sheet, (0, 0), rect)
        return image

    def images_at(self, rects):
        """Extract multiple images from the sprite sheet given a list of rectangles."""
        return [self.image_at(rect) for rect in rects]

    def load_strip(self, rect, image_count):
        """Extract a horizontal strip of images from the sprite sheet."""
        return [self.image_at((rect[0] + rect[2] * x, rect[1], rect[2], rect[3])) for x in range(image_count)]

    def load_grid(self, rect, columns, rows):
        """
        Load a grid of images from the sprite sheet.
        
        Args:
            rect: (x, y, width, height) defining the top-left of the grid and size of each cell.
            columns: Number of columns in the grid.
            rows: Number of rows in the grid.
        
        Returns:
            A list of images in row-major order.
        """
        grid_images = []
        for row in range(rows):
            for col in range(columns):
                x = rect[0] + col * rect[2]
                y = rect[1] + row * rect[3]
                grid_images.append(self.image_at((x, y, rect[2], rect[3])))
        return grid_images
    