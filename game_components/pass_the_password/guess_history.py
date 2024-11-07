import pygame

class GuessHistory(pygame.sprite.Sprite):
    def __init__(self, start_x = 50, feedback_x=300, line_height=35, color=(255, 255, 255)):
        """
        Initialize the GuessHistory sprite.
        
        Parameters:
        - font: The font to use for rendering text.
        - width: Width of the history surface.
        - height: Height of the history surface.
        - start_x: The x-coordinate to start drawing the guess text.
        - feedback_x: The x-coordinate to start drawing the feedback text.
        - line_height: The vertical spacing between each guess line.
        - color: The color of the text.
        """
        super().__init__()
        self.font = pygame.font.Font(None, 28)
        self.width = 1024
        self.height = 175
        self.start_x = start_x
        self.feedback_x = feedback_x
        self.line_height = line_height
        self.color = color
        self.guess_history = []  # List to store the history of guesses
        
        # Create the surface and rect for the sprite
        self.image = pygame.Surface((1024, 175), pygame.SRCALPHA)  # Transparent background
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 576)

    def add_guess(self, guess, correct_count):
        """Add a new guess to the history and update the display."""
        self.guess_history.append((guess, correct_count))
        self.update_image()

    def update_image(self):
        """Redraw the image with the current guess history."""
        self.image.fill((0, 0, 0, 0))  # Clear the surface with transparency
        
        # Calculate starting y position based on the number of guesses
        history_start_y = self.height - (len(self.guess_history) * self.line_height)

        for index, (past_guess, correct_count) in enumerate(self.guess_history):
            # Render guess and feedback text
            guess_text = self.font.render(f"Guess {index + 1}: {''.join(map(str, past_guess))}", True, self.color)
            feedback_text = self.font.render(f"Correct positions: {correct_count}", True, self.color)
            
            # Blit text to the image surface at the calculated positions
            self.image.blit(guess_text, (self.start_x, history_start_y + index * self.line_height))
            self.image.blit(feedback_text, (self.feedback_x, history_start_y + index * self.line_height))

    def reset(self):
        """Clear the guess history and update the display."""
        self.guess_history.clear()
        self.update_image()