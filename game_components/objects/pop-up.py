import pygame
from .button import Button

class Popup:
    def __init__(self, text, width, height):
        self.text = text
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 28)
        self.visible = True

        # Popup dimensions and position
        self.rect = pygame.Rect(100, 100, width, height)
        
        # Close button ("X" at top right)
        self.close_button_rect = pygame.Rect(self.rect.right - 30, self.rect.top + 10, 20, 20)

        # Buttons for user actions
        self.button1 = Button("OK", self.rect.x + 30, self.rect.y + height - 60, 80, 40)
        self.button2 = Button("Cancel", self.rect.x + width - 110, self.rect.y + height - 60, 80, 40)

    def on_ok(self):
        print("OK clicked")
        self.visible = False

    def on_cancel(self):
        print("Cancel clicked")
        self.visible = False

    def draw(self, screen):
        if not self.visible:
            return

        # Draw popup background and border
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        # Draw close "X" button
        pygame.draw.rect(screen, (255, 0, 0), self.close_button_rect)
        close_text = self.font.render("X", True, (255, 255, 255))
        screen.blit(close_text, (self.close_button_rect.x + 3, self.close_button_rect.y))

        # Draw popup text
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 20))

        # Draw buttons
        self.button1.draw(screen)
        self.button2.draw(screen)

    def handle_event(self, event):
        if not self.visible:
            return

        # Handle close button
        if event.type == pygame.MOUSEBUTTONDOWN and self.close_button_rect.collidepoint(event.pos):
            self.visible = False

        # Handle buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)