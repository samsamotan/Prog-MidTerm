import pygame
from ..objects import *
from ..scene import Scene
import os
from ..main_scene.walls import rects

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class MainScene(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 2048
        height = 1638
        super().__init__(scene_manager, game_state, audio_manager, width, height)

    def start(self):
        background = GameObject(0, 0, image = os.path.join(assets_folder, "map1.png"))
        self.player = Player(1000, 500, 15, 20, os.path.join(assets_folder, "cowboy.png"))
        npc1 = NPC(200, 150,
                    ["Ralof: Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there.", 
                     "Lokir: Damn you Stormcloaks. Skyrim was fine until you came along. Empire was nice and lazy. If they hadn't been looking for you, I could've stolen that horse and been half way to Hammerfell. You there. You and me -- we should be here. It's these Stormcloaks the Empire wants.", 
                     "Ralof: We're all brothers and sisters in binds now, thief.", "Imperial Soldier: Shut up back there!", 
                     "Lokir: And what's wrong with him?", "Ralof: Watch your tongue! You're speaking to Ulfric Stormcloak, the true High King.", 
                     "Lokir: Ulfric? The Jarl of Windhelm? You're the leader of the rebellion. But if they captured you... Oh gods, where are they taking us?", 
                     "Ralof: I don't know where we're going, but Sovngarde awaits.", 
                     "Lokir: No, this can't be happening. This isn't happening.",
                     "Ralof: Hey, what village are you from, horse thief?", 
                     "Lokir: Why do you care?", 
                     "Ralof: A Nord's last thoughts should be of home.", 
                     "Lokir: Rorikstead. I'm...I'm from Rorikstead."])
        portal_to_vacuum = InteractiveObject(300, 300, 50, 30, self.scene_manager, "Main Scene", "Virus Vacuum", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_vacuum.add_action(pygame.K_e, "change scene")
        portal_to_firewall = InteractiveObject(400, 300, 50, 30, self.scene_manager, "Main Scene", "Firewall Fighter", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_firewall.add_action(pygame.K_e, "change scene")
        portal_to_password = InteractiveObject(500, 300, 50, 30, self.scene_manager, "Main Scene", "Pass the Password", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_password.add_action(pygame.K_e, "change scene")
        portal_to_packets = InteractiveObject(600, 300, 50, 30, self.scene_manager, "Main Scene", "Packing Packets", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_packets.add_action(pygame.K_e, "change scene")
        portal_to_color = InteractiveObject(700, 300, 50, 30, self.scene_manager, "Main Scene", "Color Match", os.path.join(assets_folder, "pixil-frame-0.png"))
        portal_to_color.add_action(pygame.K_e, "change scene")
        walls = [GameObject(x[0],x[1],x[2],x[3]) for x in rects]
        self.interactions.add(portal_to_vacuum, portal_to_firewall, portal_to_password, portal_to_packets, portal_to_color)
        self.all_sprites.add(background, walls, npc1, portal_to_vacuum, portal_to_firewall, portal_to_password, portal_to_packets, portal_to_color)
        self.obstacles.add(walls)
        self.npc_group = pygame.sprite.Group()
        self.npc_group.add(npc1)

    def handle_events(self, dt):
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self, self.obstacles)
        for event in self.game_state.get_events():
            for npc in self.npc_group:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if npc.in_proximity:
                        npc.start_conversation()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and npc.chatbox.active:
                    npc.chatbox.next_message()

    def update(self, dt):
        for npc in self.npc_group:
            npc.update(self.player.rect.center)
            npc.chatbox.update()

    def draw(self, screen, camera):
        print(self.player.rect)
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        for npc in self.npc_group:
            npc.draw_prompt(screen, camera)
            npc.draw_chatbox(screen, camera)
        screen.blit(self.player.image, camera.apply(self.player.rect))