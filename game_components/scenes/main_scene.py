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
        self.player = BigPlayer(1000, 600, 15, 20, os.path.join(assets_folder, "cowboy.png"))
        if self.game_state.player_pos != (1000, 600):
            self.player.set_pos(self.game_state.player_pos)
            self.game_state.player_pos = (1000, 600)
        else:
            pass
        virus_vacuum_npc = NPC(830, 1180, 75, 75,
                    [
                        "Uh-oh! Your computer has some viruses. Collect all the viruses without getting caught to make the system safe.", 
                        "You are too slow to catch up to them but that's no problem. Use your mouse pointer to change the walls.",
                        "Remember, use WASD to move."
                     ], self, "Virus Vacuum", os.path.join(assets_folder, "npcs", "indian_woman.png"))
        cat = NPC(970, 380, 50, 50, ["Meow", "Meow", "Meow", "Meow", "Meow"], self, "Color Match")
        firewall_fighter_npc = NPC(1500, 1480, 75, 75,
                    [
                        "There are some viruses coming. Go take them down",
                        "Use the WASD to move left and right and spacebar to blast the viruses away.",
                        "" 
                     ], self, "Firewall Fighter", os.path.join(assets_folder, "npcs", "uncle_fisherman.png"))
        self.password_npc = NPC(2225, 1625, 75, 75,
                    [
                        "It's no use trying. The door is locked well, you have a better chance trying to guess the password",
                        "You'll have to move around with WASD and press space bar above a number.",
                         "Remember, each digit will only appear once."
                     ], self, "Pass the Password", os.path.join(assets_folder, "npcs", "chinese_woman.png"))
        self.packing_packets_npc = NPC(1920, 1425, 75, 75,
                    [
                        "The file you're looking for is hidden here somewhere. Sort out all the files here and it should show itself"
                     ], self, "Packing Packets", os.path.join(assets_folder, "npcs", "village_head.png"))
        walls = [GameObject(x[0],x[1],x[2],x[3], alpha=0) for x in rects]
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.scene_manager.start_scene("Start Scene")

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
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.game_state.camera.apply(sprite.rect))
        for npc in self.npc_group:
            npc.draw_prompt(screen, self.game_state.camera)
            npc.draw_chatbox(screen)
        screen.blit(self.player.image, self.game_state.camera.apply(self.player.rect))