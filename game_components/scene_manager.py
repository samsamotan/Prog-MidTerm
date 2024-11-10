class SceneManager:
    def __init__(self, game_state, audio_manager):
        self.scenes = {}
        self.game_state = game_state
        self.audio_manager = audio_manager

    def add_scene(self, scene_name, scene_class):
        self.scenes[scene_name] = scene_class
    
    def start_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name](self, self.game_state, self.audio_manager)
        self.current_scene.start()

    def handle_events(self, dt):
        self.current_scene.handle_events(dt)

    def update(self, camera, screen, dt):
        try:
            camera.update(self.current_scene.player, self.current_scene, screen)
        except:
            pass
        self.current_scene.update(dt)
    
    def draw(self, screen):
         self.current_scene.draw(screen)