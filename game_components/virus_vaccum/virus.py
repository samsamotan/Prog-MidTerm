import pygame
import random
from ..objects.game_object import GameObject

class Virus(GameObject):
    def __init__(self, map, image:str = None):
        x, y = self.choose_spawn_point(map, {"x_min": 16, "x_max": 19, "y_min": 8, "y_max": 11})
        super().__init__(x * 32 + 8, y * 32 + 6, 15, 20, image)
        self.speed = 150
        self.new_pos = self.rect.topleft
        self.direction = None
        self.choose_direction(map)

    def choose_spawn_point(self, map, exclusion_zone = None):
        """Choose a random spawn point that is a free tile on the map,
        avoiding a specified exclusion zone.
        """
        map_width, map_height = len(map.wallgrid[0]), len(map.wallgrid)

        # Set exclusion bounds, defaulting to none if not provided
        x_ex_min = exclusion_zone.get("x_min", -1) if exclusion_zone else -1
        x_ex_max = exclusion_zone.get("x_max", map_width) if exclusion_zone else map_width
        y_ex_min = exclusion_zone.get("y_min", -1) if exclusion_zone else -1
        y_ex_max = exclusion_zone.get("y_max", map_height) if exclusion_zone else map_height

        # Find all free tiles outside the exclusion zone
        free_tiles = [
            (x, y) for x in range(map_width) for y in range(map_height)
            if not map.get_wallgrid_value(x, y) and not (x_ex_min <= x <= x_ex_max and y_ex_min <= y <= y_ex_max)
        ]

        # Choose a random free tile outside the exclusion zone
        if free_tiles:
            return random.choice(free_tiles)
        else:
            raise ValueError("No valid spawn points available outside the exclusion zone.")

    def move(self, dt, map, player):
        """Moves the virus and checks for collision with player sprites."""
        self.update_position(dt)

        # If virus has reached target position, choose a new direction
        if self.rect.topleft == self.new_pos:
            self.choose_direction(map)
            self.set_new_pos()

        # Check collision with player sprites in the player group
        return self.rect.colliderect(player)

    def update_position(self, dt):
        """Updates the virus position based on the current direction."""
        if self.new_pos[0] != self.rect.x:
            direction = 1 if self.new_pos[0] > self.rect.x else -1
            self.rect.x += direction * min(abs(self.new_pos[0] - self.rect.x), self.speed * dt)
        elif self.new_pos[1] != self.rect.y:
            direction = 1 if self.new_pos[1] > self.rect.y else -1
            self.rect.y += direction * min(abs(self.new_pos[1] - self.rect.y), self.speed * dt)

    def choose_direction(self, map):
        """Chooses a new direction based on possible moves in the map."""
        grid_pos = (self.rect.x // 32, self.rect.y // 32)
        possible_directions = []

        if grid_pos[0] > 0 and not map.get_wallgrid_value(grid_pos[0] - 1, grid_pos[1]):
            possible_directions.append("west")
        if grid_pos[0] < 31 and not map.get_wallgrid_value(grid_pos[0] + 1, grid_pos[1]):
            possible_directions.append("east")
        if grid_pos[1] > 0 and not map.get_wallgrid_value(grid_pos[0], grid_pos[1] - 1):
            possible_directions.append("north")
        if grid_pos[1] < 15 and not map.get_wallgrid_value(grid_pos[0], grid_pos[1] + 1):
            possible_directions.append("south")

        # Avoid going back in the opposite direction when possible
        if len(possible_directions) > 1 and self.direction:
            opposite = self.get_opposite_direction(self.direction)
            if opposite in possible_directions:
                possible_directions.remove(opposite)

        # Choose a random direction from the remaining possibilities
        self.direction = random.choice(possible_directions) if possible_directions else self.direction

    def get_opposite_direction(self, direction):
        """Returns the opposite direction."""
        opposites = {"north": "south", "south": "north", "east": "west", "west": "east"}
        return opposites.get(direction)

    def set_new_pos(self):
        """Sets the new target position based on the current direction."""
        movement_map = {
            "north": (0, -32),
            "south": (0, 32),
            "west": (-32, 0),
            "east": (32, 0)
        }
        dx, dy = movement_map.get(self.direction, (0, 0))
        self.new_pos = (self.rect.x + dx, self.rect.y + dy)