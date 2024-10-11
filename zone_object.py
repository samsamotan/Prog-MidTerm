class ZoneObject():
    def __init__(self, size_x, size_y, init_x=0, init_y=0, colliding = False):
        self.pos = {"X": init_x, "Y": init_y}
        self.size = {"X": size_x, "Y": size_y}
        self.colliding = colliding
    def get_x_pos(self):
        return self.pos["X"]
    def get_y_pos(self):
        return self.pos["Y"]
    def get_x_size(self):
        return self.size["X"]
    def get_y_size(self):
        return self.size["Y"]
    def is_colliding(self):
        return self.colliding
    def within(self, x, y):
        if (x > self.pos["X"] and x < self.pos["X"] + self.size["X"] and y > self.pos["Y"] and y < self.pos["Y"] + self.size["Y"]):
            return True
        else:
            return False 
    