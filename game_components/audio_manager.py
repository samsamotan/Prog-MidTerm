import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()  # Initialize the mixer module
        self.sounds = {}     # Dictionary to store loaded sounds by name
        self.currently_playing = None

    def load(self, name, file_path):
        """Loads a sound file and stores it by name."""
        sound = pygame.mixer.Sound(file_path)
        self.sounds[name] = sound

    def play(self, name, loops=0):
        """Plays a loaded sound."""
        if name in self.sounds:
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