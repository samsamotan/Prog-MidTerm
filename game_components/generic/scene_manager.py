class SceneManager():
    def __init__(self, active_scene):
        self.active_scene = active_scene
    def get_scene(self):
        return self.active_scene
    def set_scene(self, new_scene):
        self.active_scene = new_scene