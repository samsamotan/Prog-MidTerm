import pygame
from ..objects import *
from ..scene import Scene
import os
from ..main_scene.walls import rects

assets_folder = os.path.join(os.path.dirname(__file__), "..",  "..", "assets")

class MainScene(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 3200
        height = 2560
        super().__init__(scene_manager, game_state, audio_manager, width, height)

    def start(self):
        self.audio_manager.play("main_scene_music", -1)
        background = GameObject(0, 0, image = os.path.join(assets_folder, "map1.png"))
        self.player = Player(1000, 600, 15, 20, os.path.join(assets_folder, "cowboy.png"))
        if self.game_state.player_pos != (1000, 600):
            self.player.set_pos(self.game_state.player_pos)
            self.game_state.player_pos = (1000, 600)
        else:
            pass
        virus_vacuum_npc = NPC(830, 1180, 150, 150,
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
                     "Lokir: Rorikstead. I'm...I'm from Rorikstead."], self, "Virus Vacuum", os.path.join(assets_folder, "npcs", "indian_woman.png"))
        cat = NPC(970, 380, 50, 50, ["Meow", "Meow", "Meow", "Meow", "Meow"], self, "Color Match")
        firewall_fighter_npc = NPC(1500, 1480, 150, 150,
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
                     "Lokir: Rorikstead. I'm...I'm from Rorikstead."], self, "Firewall Fighter", os.path.join(assets_folder, "npcs", "uncle_fisherman.png"))
        self.password_npc = NPC(2225, 1625, 150, 150,
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
                     "Lokir: Rorikstead. I'm...I'm from Rorikstead."], self, "Pass the Password", os.path.join(assets_folder, "npcs", "chinese_woman.png"))
        self.packing_packets_npc = NPC(1920, 1425, 150, 150,
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
                     "Lokir: Rorikstead. I'm...I'm from Rorikstead."], self, "Packing Packets", os.path.join(assets_folder, "npcs", "village_head.png"))
        walls = [GameObject(x[0],x[1],x[2],x[3]) for x in rects]
        barrier_image = pygame.transform.scale_by(pygame.image.load(os.path.join(assets_folder, "pixil-frame-0.png")),1.5)
        self.barrier = GameObject(2015,1585,image = barrier_image)
        self.all_sprites.add(background, self.barrier, walls, virus_vacuum_npc, firewall_fighter_npc, self.password_npc, self.packing_packets_npc, cat)
        self.obstacles.add(self.barrier, walls, virus_vacuum_npc, firewall_fighter_npc, self.password_npc, self.packing_packets_npc, cat)
        self.npc_group = pygame.sprite.Group()
        self.npc_group.add(virus_vacuum_npc, firewall_fighter_npc, self.password_npc, self.packing_packets_npc, cat)

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
            npc.update(self.player.rect.center, dt)
            npc.chatbox.update()
        if self.game_state.passed == True:
            self.barrier.kill()
            self.password_npc.in_proximity = False
        else:
            self.packing_packets_npc.in_proximity = False

    def draw(self, screen):
        print(self.player.rect)
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.game_state.camera.apply(sprite.rect))
        for npc in self.npc_group:
            npc.draw_prompt(screen, self.game_state.camera)
            npc.draw_chatbox(screen)
        screen.blit(self.player.image, self.game_state.camera.apply(self.player.rect))