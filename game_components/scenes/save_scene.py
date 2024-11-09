from ..scene import Scene
from ..objects import *
import pygame

BLACK = (0, 0, 0)

class SaveScene(Scene):
    def __init__(self, scene_manager, game_state, audio_manager):
        width = 1024
        height = 576
        super().__init__(scene_manager, game_state, audio_manager, width, height)

    def start(self):
        pass

    def handle_events(self, events):
        return super().handle_events(events)
    
    def update(self, dt):
        return super().update(dt)
    
    def draw(self, screen):
        # Draw the same background image used in the main menu
        screen.blit(background, (0, 0))
        
        for i, slot in enumerate(save_slots_info):
            # Draw semi-transparent slot box with rounded corners
            slot_surf = pygame.Surface((400, 100), pygame.SRCALPHA)  # SRCALPHA allows transparency
            slot_surf.fill(slot_box_color)  # Fill with semi-transparent color
            pygame.draw.rect(slot_surf, BLACK, slot_surf.get_rect(), width=2, border_radius=15)  # Border
            
            # Blit the slot box to the main screen with an offset
            screen.blit(slot_surf, (200, 150 + i * 120))
            
            # Draw slot name with smaller font
            name_surf = slot_name_font.render(slot["name"], True, BLACK)
            screen.blit(name_surf, (210, 160 + i * 120))
            
            # Draw minigame icons (grayed out if not complete)
            for j, icon in enumerate(slot["minigame_icons"]):
                if icon:
                    icon_x = 210 + j * (icon_size[0] + 5)
                    icon_y = 190 + i * 120
                    screen.blit(icon, (icon_x, icon_y))
            
            # Draw character image if available
            if slot["character_image"]:
                screen.blit(slot["character_image"], (480, 170 + i * 120))
            
            # Draw status text (e.g., "Incomplete" or "Empty")
            status_surf = back_font.render(slot["status"], True, BLACK)
            screen.blit(status_surf, (400, 160 + i * 120))
        
        # Draw back button
        screen.blit(back_surf, back_rect)