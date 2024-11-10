from ..scene import Scene

class Opening(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)

    def start(self):
        return super().start()
    
    def handle_events(self, events):
        return super().handle_events(events)
    
    def draw(self, screen):
        return super().draw(screen)