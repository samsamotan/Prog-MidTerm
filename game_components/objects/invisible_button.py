from .button import Button

GRAY = (0,0,0,0)
BLACK = (0, 0, 0)

class InvisibleButton(Button):
    def __init__(self, x, y, width, height, color=GRAY, text_color=BLACK):
        super().__init__("", x, y, width, height, color, text_color)