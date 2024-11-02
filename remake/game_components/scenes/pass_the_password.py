import pygame as pg
from ..objects import *
from ..pass_the_password import *
from ..scene import Scene
import os
import random

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class PassThePassword(Scene):
    def __init__(self, scene_manager, game_state):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, width, height)
        self.guesses = []
        self.guess = []
        

    def start(self):
        self.player = Player(50, 50, 15, 20)
        self.background = GameObject(0, 0, self.width, self.height, os.path.join(assets_folder, "bg.png"))
        buttons = [Button(self.width/2 - 190 + i*100, self.height/2, 80, 80, f"{i}") for i in range(4)]
        self.all_sprites.add(self.background, buttons)

    def handle_events(self, dt):
        for interaction in self.interactions:
            interaction.interact(self.game_state.get_events(), self.player)
        self.player.move(self.game_state.get_keys(), dt, self)


    def draw(self, screen, camera):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, camera.apply(sprite.rect))
        screen.blit(self.player.image, camera.apply(self.player.rect))

    def generate_random_password(self):
        return random.sample([1, 2, 3, 4], k=4)
    
    