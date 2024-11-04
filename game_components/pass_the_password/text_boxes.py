import pygame as pg

class CurrentGuess(pg.sprite.Sprite):
    def __init__(self, text, center_position):
        """
        Initialize the TextSprite.

        Parameters:
        - text: The initial text to display.
        - font: The font used to render the text.
        - color: The color of the text.
        - center_position: The position to center the text on screen.
        """
        super().__init__()
        self.font = pg.font.Font(None, 48)
        self.color = (255, 255, 255)
        self.center_position = center_position
        self.update_text(text)

    def update_text(self, new_text):
        """Update the text content and re-render the image."""
        self.text = "Your guess: " + new_text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.center_position)

class CorrectNumber(pg.sprite.Sprite):
    def __init__(self, text, center_position):
        """
        Initialize the TextSprite.

        Parameters:
        - text: The initial text to display.
        - font: The font used to render the text.
        - color: The color of the text.
        - center_position: The position to center the text on screen.
        """
        super().__init__()
        self.font = pg.font.Font(None, 48)
        self.color = (255, 255, 255)
        self.center_position = center_position
        self.update_text(text)

    def update_text(self, new_text):
        """Update the text content and re-render the image."""
        self.text = new_text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.center_position)

class TriesRemaining(pg.sprite.Sprite):
    def __init__(self, text, center_position):
        """
        Initialize the TextSprite.

        Parameters:
        - text: The initial text to display.
        - font: The font used to render the text.
        - color: The color of the text.
        - center_position: The position to center the text on screen.
        """
        super().__init__()
        self.font = pg.font.Font(None, 48)
        self.color = (255, 255, 255)
        self.center_position = center_position
        self.update_text(text)

    def update_text(self, new_text):
        """Update the text content and re-render the image."""
        self.text = "Tries left: " + new_text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.center_position)