import sys
from pathlib import Path
src_dir = str(Path(__file__).resolve().parent.parent.parent)
if src_dir not in sys.path:
    sys.path.append(src_dir)
    
from game_components.generic import character
import math
import random

class Virus(character.Character):
    def __init__(self, *args, map):
        super().__init__(*args)
        self.new_pos = {"X":self.pos["X"],"Y":self.pos["Y"]}
        self.speed = 200
        self.choose_direction(map)

    def move(self, dt, map):
        if self.new_pos["X"] == self.pos["X"] and self.new_pos["Y"] == self.pos["Y"]:
            self.choose_direction(map)
            self.set_new_pos()
        elif self.new_pos["X"] != self.pos["X"]:
            if self.new_pos["X"] > self.pos["X"]:
                if self.new_pos["X"] - self.pos["X"] > self.speed * dt:
                    self.pos["X"] = self.pos["X"] + self.speed * dt
                else:
                    self.pos["X"] = self.new_pos["X"]
            elif self.new_pos["X"] < self.pos["X"]:
                if self.pos["X"] - self.new_pos["X"] > self.speed * dt:
                    self.pos["X"] = self.pos["X"] - self.speed * dt
                else:
                    self.pos["X"] = self.new_pos["X"]
        elif self.new_pos["Y"] != self.pos["Y"]:
            if self.new_pos["Y"] > self.pos["Y"]:
                if self.new_pos["Y"] - self.pos["Y"] > self.speed * dt:
                    self.pos["Y"] = self.pos["Y"] + self.speed * dt
                else:
                    self.pos["Y"] = self.new_pos["Y"]
            elif self.new_pos["Y"] < self.pos["Y"]:
                if self.pos["Y"] - self.new_pos["Y"] > self.speed * dt:
                    self.pos["Y"] = self.pos["Y"] - self.speed * dt
                else:
                    self.pos["Y"] = self.new_pos["Y"]

    def choose_direction(self, map):
        pos = [math.floor(self.pos["X"]/32), math.floor(self.pos["Y"]/32)]
        possible_directions = []
        try:
            if not map.get_wallgrid_value(pos[0]-1,pos[1]) and pos[0] != 0:
                print((pos[0]-1,pos[1]),map.get_wallgrid_value(pos[0]-1,pos[1]))
                possible_directions.append("west")
        except:
            pass
        try:
            if not map.get_wallgrid_value(pos[0]+1,pos[1]) and pos[0] != 31:
                print((pos[0]+1,pos[1]),map.get_wallgrid_value(pos[0]+1,pos[1]))
                possible_directions.append("east")
        except:
            pass
        try:
            if not map.get_wallgrid_value(pos[0],pos[1]-1) and pos[1] != 0:
                print((pos[0],pos[1]-1),map.get_wallgrid_value(pos[0],pos[1]-1))
                possible_directions.append("north")
        except:
            pass
        try:
            if not map.get_wallgrid_value(pos[0],pos[1]+1) and pos[1] != 15:
                print((pos[0],pos[1]+1),map.get_wallgrid_value(pos[0],pos[1]+1))
                possible_directions.append("south")
        except:
            pass
        print(possible_directions)
        match len(possible_directions):
            case 1:
                self.direction = possible_directions[0]
            case 2:
                chooser = random.randint(1,10)
                #if chooser < 9:
                try:
                    possible_directions.remove(self.get_opposite_direction(self.direction))
                except:
                    pass
                self.direction = possible_directions[0]
                #else:
                 #   self.direction = self.get_opposite_direction(self.direction)
            case 3:
                chooser = random.randint(1,10)
                #if chooser < 10:
                try:
                    possible_directions.remove(self.get_opposite_direction(self.direction))
                except:
                    pass
                self.direction = possible_directions[random.randint(0,1)]
                #else:
                 #   self.direction = self.get_opposite_direction(self.direction)
            case 4:
                self.direction = possible_directions[random.randint(0,3)]
    
    def get_opposite_direction(self, direction):
        match direction:
            case "north":
                return "south"
            case "south":
                return "north"
            case "east":
                return "west"
            case "west":
                return "east"
    
    def set_new_pos(self):
        match self.direction:
            case "north":
                self.new_pos["Y"] = self.pos["Y"] - 32
            case "south":
                self.new_pos["Y"] = self.pos["Y"] + 32
            case "west":
                self.new_pos["X"] = self.pos["X"] - 32
            case "east":
                self.new_pos["X"] = self.pos["X"] + 32
        
        print(self.direction, self.new_pos, self.pos)
