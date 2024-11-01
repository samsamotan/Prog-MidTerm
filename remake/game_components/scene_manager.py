class SceneManager:
    def __init__(self, start_scene):
        self.scenes = {}
        self.current_scene = start_scene
        self.start_scene(start_scene)

    def add_scene(self, scene_name, scene_class):
        self.scenes[scene_name] = scene_class
    
    def start_scene(self, scene_name):
        if scene_name in self.scenes:
            if isinstance(self.scenes[scene_name], type):
                self.current_scene = self.scenes[scene_name](self)
                self.scenes[scene_name] = self.current_scene
            else:
                self.current_scene = self.scenes[scene_name]

            self.current_scene.start()

    def reset_scene(self, scene_name):
        if scene_name in self.scenes:
            if not isinstance(self.scenes[scene_name], type):
                self.scenes[scene_name] = type(self.scenes[scene_name])

    def handle_events(self, events, keys, dt):
        self.current_scene.handle_events(events, keys, dt)

    def update(self):
        self.current_scene.update()
    
    def draw(self, screen):
         self.current_scene.draw(screen)