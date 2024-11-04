from .game_object import GameObject

class SpriteTile(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, image:str = None, is_wall:bool = False):
        super().__init__(x, y, width, height, image)
        self.is_wall = is_wall

    def is_wall(self):
        return self.is_wall