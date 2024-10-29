import pygame as pg

class Scene():
    def __init__(self, has_tilemap, bg, objects, x = 0, y = 0):
        self.scene_objects = objects
        self.hitboxes = []
        if has_tilemap: 
            self.map = bg
            self.map_height = y
            self.map_width = x
            for tile in bg.get_tiles():
                if tile.is_colliding():
                    self.hitboxes.append(tile.get_hitbox())
        else:
            self.map_image = pg.image.load(bg)     
            self.map_width, self.map_height = self.map_image.get_size()
        for object in objects:
            if object.is_colliding():
                self.hitboxes.append(object.get_hitbox())
    def set_hitboxes(self):
        self.hitboxes = []
        for tile in self.map.get_tiles():
            if tile.is_colliding():
                self.hitboxes.append(tile.get_hitbox())
        for object in self.scene_objects:
            if object.is_colliding():
                self.hitboxes.append(object.get_hitbox())
    def get_height(self):
        return self.map_height
    def get_hitboxes(self):
        return self.hitboxes
    def get_width(self):
        return self.map_width
    def get_objects(self):
        return self.scene_objects
    def render(self, screen, camera, player):

        # background
        screen.fill((0, 0, 0))
        try:
            screen.blit(self.map_image, (-camera.get_x_pos(), -camera.get_y_pos()))
        except:
            for tile in self.map_image:
                screen.blit(tile.get_image(), (tile.get_x_pos() - tile.get_x_pos(), tile.get_y_pos() - tile.get_y_pos()))
                
        # objects
        for object in self.scene_objects:
            screen.blit(object.get_image(), (object.get_x_pos() - camera.get_x_pos(), object.get_y_pos() - camera.get_y_pos()))
            
        # player
        pg.draw.rect(screen, (255, 0, 0), (player.get_x_pos() - camera.get_x_pos(), player.get_y_pos() - camera.get_y_pos(), player.get_x_size(), player.get_y_size()))
       
        # flip() the display to put your work on screen
        #pg.display.flip()
