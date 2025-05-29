import pygame
import os
import config as c
import assets as a

## class defined 
# class for start screen
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

# class for button
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

# class for toggle image
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

## function defined 
# funct for unlock the screen
def activate_motion():
    pygame.event.set_grab(False)  # Allow mouse movement
    pygame.event.set_allowed(pygame.MOUSEMOTION)      # Allow mouse movement
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)  # Allow mouse click
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)    # Optional: allow mouse release
    pygame.event.set_allowed(pygame.KEYDOWN)          # Allow key presses
    pygame.event.set_allowed(pygame.KEYUP)            # Optional: allow key releases

# funct for lock the screen
def deactivate_motion():
    pygame.event.set_blocked(pygame.MOUSEMOTION)      # Ignore mouse movement
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)  # Ignore mouse click
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)    # Optional: ignore mouse release
    pygame.event.set_blocked(pygame.KEYDOWN)          # Ignore key presses
    pygame.event.set_blocked(pygame.KEYUP) 

# func to swtich the screen
def screen_switch(screen, frame, size, pos, color_filled, index = 0, speed=0.025):
    screen.fill(color_filled)
    index += speed

    if index >= len(frame):
        index = 0

    current = frame[int(index)]
    current = pygame.transform.scale(current, size)
    screen.blit(current, pos)

    return index

# func to draw the text
def draw_text(text, x, y, color, font, screen):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)
    return rect

