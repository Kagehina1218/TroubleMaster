import pygame
import os
import config as c
import assets as a

class StartScreen:
    def __init__(self, screen, frames):
        self.screen = screen
        self.frames = frames
        
        # Set the current frame
        self.current_frame = 0

        # Animation timing
        self.animation_speed = 500  
        self.last_switch_time = pygame.time.get_ticks()

        # Button rect (adjust to match your image)
        self.button_rect = pygame.Rect(135,325,200,80)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                return "started"
        return None

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_switch_time = current_time

    def draw(self):
        self.screen.blit(self.frames[self.current_frame], (0, 0))


class Button:
    def __init__(self, screen, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.screen = screen

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return "clicked"
        return None

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def show_frame(self, image):
        global current
        current = image

class ToggleImage:
    def __init__(self, pos, images):
        self.images = images
        self.index = 0
        self.rect = self.images[0].get_rect(topleft=pos)

    def draw(self, surface):
        surface.blit(self.images[self.index], self.rect)

    def handle_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.index = 1 - self.index  


def shiba_animation():
        # play walking animation
    global shiba_index, shiba_surface
        # walking animation
    shiba_index += 0.1
    if shiba_index >= len(c.shiba_walk): shiba_index =0
    shiba_surface = c.shiba_walk[int(shiba_index)]

def activate_motion():
    pygame.event.set_grab(False)  # Allow mouse movement
    pygame.event.set_allowed(pygame.MOUSEMOTION)      # Allow mouse movement
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)  # Allow mouse click
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)    # Optional: allow mouse release
    pygame.event.set_allowed(pygame.KEYDOWN)          # Allow key presses
    pygame.event.set_allowed(pygame.KEYUP)            # Optional: allow key releases

def deactivate_motion():
    pygame.event.set_blocked(pygame.MOUSEMOTION)      # Ignore mouse movement
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)  # Ignore mouse click
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)    # Optional: ignore mouse release
    pygame.event.set_blocked(pygame.KEYDOWN)          # Ignore key presses
    pygame.event.set_blocked(pygame.KEYUP) 

def display_text_block(self, text_list, theScreen, theFont, y_bottom=780, padding=20, alpha=150):
    """
    Displays a list of text lines stacked vertically with a transparent background behind them.
    """
    # Render all text lines and store their surfaces and rects
    text_surfs = [c.font.render(line, True, (255, 255, 255)) for line in text_list]
    text_rects = [surf.get_rect() for surf in text_surfs]

    # Calculate the total height of the stacked text
    spacing = 5  # space between lines
    total_text_height = sum(rect.height for rect in text_rects) + spacing * (len(text_list) - 1)

    # Starting y position for the first line (aligned to y_bottom)
    start_y = y_bottom - total_text_height

    # Find the widest line for background width
    max_width = max(rect.width for rect in text_rects)

    # Create the background surface
    bg_width = max_width + padding * 2
    bg_height = total_text_height + padding
    bg_surf = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
    bg_surf.fill((0, 0, 0, alpha))  # semi-transparent black

    # Center the background horizontally
    bg_rect = bg_surf.get_rect(centerx=theScreen.get_width() // 2, bottom=y_bottom)

    # Blit background
    theScreen.blit(bg_surf, bg_rect)

    # Blit each text line
    current_y = bg_rect.top + padding // 2
    for surf, rect in zip(text_surfs, text_rects):
        rect.midtop = (theScreen.get_width() // 2, current_y)
        theScreen.blit(surf, rect)
        current_y += rect.height + spacing

# class Lock:
#     def __init__(self):
#         pass

#     def lock(self):

def screen_switch(screen, frame, size, pos, color_filled, index = 0, speed=0.025):
    screen.fill(color_filled)
    index += speed

    if index >= len(frame):
        index = 0

    current = frame[int(index)]
    current = pygame.transform.scale(current, size)
    screen.blit(current, pos)

    return index

def draw_text(text, x, y, color, font, screen):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)
    return rect

