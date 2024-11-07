import pygame as pg

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Slider(pg.sprite.Sprite):
    def __init__(self, label, pos, color, min_val=0, max_val=255):
        super().__init__()
        self.label = label
        self.x, self.y = pos
        self.color = color
        self.width = 300
        self.height = 10
        self.radius = 10
        self.min_val = min_val
        self.max_val = max_val
        self.value = 0
        self.slider_rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.handle_pos = self.x  # Initial handle position

    def update(self, event):
        if self.slider_rect.collidepoint(event.pos):
                self.set_value_from_mouse(event.pos[0])

    def set_value(self, value):
        self.value = max(0, min(255, value))
        self.update_image()

    def reset_value(self):
         self.value = 0
         self.handle_pos = self.x
    def set_value_from_mouse(self, mouse_x):
        # Calculate the value based on mouse position
        relative_x = mouse_x - self.x
        self.value = int(self.min_val + (relative_x / self.width) * (self.max_val - self.min_val))
        self.value = max(self.min_val, min(self.value, self.max_val))  # Clamp to min and max
        self.handle_pos = self.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.width
    def draw(self, screen):
        # Draw the left portion of the slider bar
        left_rect = pg.Rect(self.x, self.y, self.handle_pos - self.x, self.height)
        pg.draw.rect(screen, self.color, left_rect)

        # Draw the right portion of the slider bar
        right_rect = pg.Rect(self.handle_pos, self.y, self.width - (self.handle_pos - self.x), self.height)
        pg.draw.rect(screen, (200, 200, 200), right_rect)
        # Draw handle
        pg.draw.circle(screen, (self.color), (int(self.handle_pos), self.y + self.height // 2), 10)
        # Draw text showing the current value
        font = pg.font.Font(None, 36)
        text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(text, (self.x + self.width + 20, self.y - 5))