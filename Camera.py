import pygame
import character, scene

class Camera():
    def __init__(self, init_x=0, init_y=0):
        self.pos = {"X": init_x, "Y": init_y}
    def get_x_pos(self):
        return self.pos["X"]
    def get_y_pos(self):
        return self.pos["Y"]
    def update(self, player, screen, scene):
        if player.get_x_pos() < screen.get_width() / 2:
            self.pos["X"] = 0
        elif player.get_x_pos() > scene.get_width() - screen.get_width() / 2:
            self.pos["X"] = scene.get_width() - screen.get_width()
        else:
            self.pos["X"] = player.get_x_pos() - screen.get_width() / 2

        if player.get_y_pos() < screen.get_height() / 2:
            self.pos["Y"] = 0
        elif player.get_y_pos() > scene.get_height() - screen.get_height() / 2:
            self.pos["Y"] = scene.get_height() - screen.get_height()
        else:
            self.pos["Y"] = player.get_y_pos() - screen.get_height() / 2