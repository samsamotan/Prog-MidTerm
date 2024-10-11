import pygame
import Character, Zones

class Camera():
    def __init__(self, camerax=0, cameray=0):
        cameraX=camerax
        cameraY=cameray
    def getXPos(self):
        return self.cameraX
    def getYPos(self):
        return self.cameraY
    def XPos(self, xpos):
        self.cameraX = xpos
    def YPos(self, ypos):
        self.cameraY = ypos
    def update(self, player, screen, camera, zone):
        if player.getXPos() < screen.get_width() // 2:
            self.XPos(0)
        elif player.getXPos() > zone.getWidth() - screen.get_width() // 2:
            self.XPos(zone.getWidth() - screen.get_width())
        else:
            self.XPos(player.getXPos() - screen.get_width() // 2) 

        if player.getYPos() < screen.get_height() // 2:
            self.YPos(0)
        elif player.getYPos() > zone.getHeight() - screen.get_height() // 2:
            self.YPos(zone.getHeight() - screen.get_height())
        else:
            self.YPos(player.getYPos() - screen.get_height() // 2)