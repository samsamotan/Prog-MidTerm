import pygame
from ..objects import *
from ..scene import Scene
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class MainScene(Scene):
    def __init__(self, scene_manager, game_state):
        width = 2000
        height = 1000
        super().__init__(scene_manager, game_state, width, height)

    def start(self):
        self.player = Player(50, 50, 15, 20)
        portal_to_vacuum = InteractiveObject(300, 300, 50, 30, self.scene_manager, "Main Scene", "Virus Vacuum", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_vacuum.add_action(pygame.K_e, "change scene")
        portal_to_firewall = InteractiveObject(400, 300, 50, 30, self.scene_manager, "Main Scene", "Firewall Fighter", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_firewall.add_action(pygame.K_e, "change scene")
        portal_to_password = InteractiveObject(500, 300, 50, 30, self.scene_manager, "Main Scene", "Pass the Password", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_password.add_action(pygame.K_e, "change scene")
        portal_to_packets = InteractiveObject(600, 300, 50, 30, self.scene_manager, "Main Scene", "Packing Packets", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_packets.add_action(pygame.K_e, "change scene")
        self.interactions.add(portal_to_vacuum, portal_to_firewall, portal_to_password, portal_to_packets)
        self.all_sprites.add(portal_to_vacuum, portal_to_firewall, portal_to_password, portal_to_packets)

    def handle_events(self, dt):
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self)


    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))