import pygame
from ..objects import *
from ..pass_the_password import *
from ..scene import Scene
import os
import random

assets_folder = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class PassThePassword(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)

        # Initialize pygame mixer

        pygame.mixer.init()

        #Load sounds
        self.background_music = pygame.mixer.music.load(os.path.join(assets_folder, "Zora's Domain - Day (The Legend of Zelda_ Breath of the Wild OST).mp3"))
        pygame.mixer.music.play(-1)



    def start(self):
        self.max_tries = 5
        self.player = Player(50, 50, 15, 20, os.path.join(assets_folder, "cowboy.png"))
        self.background = GameObject(0, 0, self.width, self.height, os.path.join(assets_folder, "password_background.png"))
        buttons = [Button(self.width/2 - 190 + i*100, 100, 80, 80, f"{i + 1}") for i in range(4)]
        for button in buttons:
            button.add_action(pygame.K_SPACE, "press")
        self.code = random.sample([1, 2, 3, 4], k=4)
        self.guesses = GuessHistory()
        self.guess = []
        self.tries_left = self.max_tries
        self.guess_text = CurrentGuess('', (self.width // 2, 220))
        self.correct_text = CorrectNumber('', (self.width // 2, 270))
        self.tries_text = TriesRemaining(str(self.max_tries), (self.width // 2, 320))
        self.interactions.add(buttons)
        self.all_sprites.add(self.background, buttons, self.guesses, self.guess_text, self.correct_text, self.tries_text)  

    def handle_events(self, dt):
        for interaction in self.interactions:
            if interaction.interact(self):
                if len(self.guess) == 4:
                    guess = ''.join(self.guess)
                    correct = self.check_guess(guess)
                    print(correct, self.code)
                    self.guesses.add_guess(guess, correct)
                    feedback_message = f"{correct} numbers in the correct position."
                    self.correct_text.update_text(feedback_message)
                    self.guess.clear()
                    print(self.guess)
                    self.tries_left -= 1
                    self.tries_text.update_text(str(self.tries_left))
                    if correct == 4:
                        self.game_state.passed = True
                        self.scene_manager.start_scene("Main Scene")
                    if self.tries_left == 0:
                        self.scene_manager.start_scene("Main Scene")
                self.guess_text.update_text(''.join(self.guess))
        self.player.move(self.game_state.get_keys(), dt, self)

    def check_guess(self, guess):
        return sum(1 for i in range(4) if guess[i] == str(self.code[i]))

    def draw(self, screen):
        screen.fill((0,0,0))
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.game_state.camera.apply(sprite.rect))
        screen.blit(self.player.image, self.game_state.camera.apply(self.player.rect))
    
    