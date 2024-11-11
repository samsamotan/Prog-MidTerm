import pygame
import os

assets_folder = os.path.join(os.path.dirname(__file__), "..", "assets")

def initialize_audio_manager():
    from game_components.audio_manager import AudioManager
    audio_manager = AudioManager()
    
class AudioManager:
    def __init__(self):
        pygame.mixer.init()  # Initialize the mixer module
        self.sounds = {
            "background_music_menu": pygame.mixer.Sound(os.path.join(assets_folder, "Goblins_Dance_(Battle).wav")),
            "start_scene_music": pygame.mixer.Sound(os.path.join(assets_folder, "Undertale Ost_ 087 - Hopes and Dreams.mp3")),
            "main_scene_music": pygame.mixer.Sound(os.path.join(assets_folder, "time_for_adventure.mp3")),
            "virus_vacuum_music": pygame.mixer.Sound(os.path.join(assets_folder, "Donkey Kong Country - Aquatic Ambience [Restored].mp3")),
            "firewall_fighter_music": pygame.mixer.Sound(os.path.join(assets_folder, "Donkey Kong Country 2 Soundtrack_ Bramble Blast.mp3")),
            "pass_the_password_music": pygame.mixer.Sound(os.path.join(assets_folder, "Zora's Domain - Day (The Legend of Zelda_ Breath of the Wild OST).mp3")),
            "packing_packets_music": pygame.mixer.Sound(os.path.join(assets_folder, "Original Tetris theme (Tetris Soundtrack).mp3")),
            "color_match_music": pygame.mixer.Sound(os.path.join(assets_folder, "Hateno Village (The Legend of Zelda_ Breath of the Wild OST).mp3"))
        }     # Dictionary to store loaded sounds by name
        self.currently_playing = None

        

    def load(self, name, file_path):
        """Loads a sound file and stores it by name."""
        sound = pygame.mixer.Sound(file_path)
        self.sounds[name] = sound

    def play(self, name, loops=0):
        """Plays a loaded sound."""
        if name in self.sounds:
            if loops == -1:  # If loops is -1, it will loop indefinitely
                self.currently_playing = self.sounds[name].play(loops=loops)
            else:
                self.currently_playing = self.sounds[name].play(loops=loops)
                
    def stop(self, name=None):
        """Stops a specific sound or all sounds if name is not provided."""
        if name:
            if name in self.sounds:
                self.sounds[name].stop()
        else:
            pygame.mixer.stop()

    def pause(self):
        """Pauses the currently playing sound."""
        if self.currently_playing:
            self.currently_playing.pause()

    def unpause(self):
        """Unpauses the currently playing sound."""
        if self.currently_playing:
            self.currently_playing.unpause()

    def set_volume(self, name, volume):
        """Sets the volume of a specific sound (0.0 to 1.0)."""
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def stop_all(self):
        """Stops all currently playing sounds."""
        pygame.mixer.stop()

    def cleanup(self):
        """Cleans up mixer resources."""
        pygame.mixer.quit()