#Each block will have a unique ID
class Block: 
    def __init__(self):
        self.id = id
#to represent the cells that the block occupies
#dictionary to store the occupied cells in the bounding grid for each rotation state
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        