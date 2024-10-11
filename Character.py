import pygame
class character():
    def __init__(self, initX=0, initY=0):
        self.character_pos = [initX, initY]
        self.character_speed = 300
    def getXPos(self):
        return self.character_pos[0]
    def getYPos(self):
        return self.character_pos[1]
    def getSpeed(self):
        return self.character_speed
    def XPos(self, xpos):
        self.character_pos[0] = xpos
    def YPos(self, ypos):
        self.character_pos[1] = ypos