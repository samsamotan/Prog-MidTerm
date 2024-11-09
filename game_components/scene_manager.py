class SceneManager:
    def __init__(self, game_state, audio_manager):
        self.scenes = {}
        self.game_state = game_state
        self.audio_manager = audio_manager

    def add_scene(self, scene_name, scene_class):
        self.scenes[scene_name] = scene_class
    
    def start_scene(self, scene_name):
        if scene_name in self.scenes:
            if isinstance(self.scenes[scene_name], type):
                self.current_scene = self.scenes[scene_name](self, self.game_state, self.audio_manager)
                self.scenes[scene_name] = self.current_scene
            else:
                self.current_scene = self.scenes[scene_name]

            self.current_scene.start()

    def reset_scene(self, scene_name):
        if scene_name in self.scenes:
            if not isinstance(self.scenes[scene_name], type):
                self.scenes[scene_name] = type(self.scenes[scene_name])

    def quit_scene(self, current_scene, new_scene):
        self.reset_scene(current_scene)
        self.start_scene(new_scene)

    def handle_events(self, dt):
        self.current_scene.handle_events(dt)

    def update(self, camera, screen, dt):
        camera.update(self.current_scene.player, self.current_scene, screen)
        self.current_scene.update(dt)
    
    def draw(self, screen, camera):
         self.current_scene.draw(screen, camera)