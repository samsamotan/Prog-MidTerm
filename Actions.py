import Character, Zones
import pygame
def move(player, keys, dt):
    if keys[pygame.K_w]:
        player.YPos(player.getYPos() - player.getSpeed() * dt)
    if keys[pygame.K_s]:
        player.YPos(player.getYPos() + player.getSpeed() * dt)
    if keys[pygame.K_a]:
        player.XPos(player.getXPos() - player.getSpeed() * dt)
    if keys[pygame.K_d]:
        player.XPos(player.getXPos() + player.getSpeed() * dt)