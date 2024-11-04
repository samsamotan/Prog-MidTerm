from ..objects.interactive_object import InteractiveObject
import pygame as pg

class Button(InteractiveObject):
    def __init__(self, x, y, width, height, text):
        image = pg.Surface((80, 80))
        image.fill((125, 0, 125))
        self.font = pg.font.Font(None, 64)
        self.text = text
        number = self.font.render(text, True, (255, 255, 255))
        image.blit(number, number.get_rect(center = image.get_rect().center))
        super().__init__(x, y, width, height, image = image)

    def interact(self, scene):
        events = scene.game_state.get_events()
        player = scene.player
        if self.rect.colliderect(player.rect):
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key in self.actions:
                        if self.actions[event.key] == "press":
                            if self.text not in scene.guess:
                                scene.guess.append(self.text)
                                return True
