import pygame
import os
import config as c
import assets as a

## class defined 
# class for start screen
class StartScreen:
    def __init__(self, screen, frames):
        '''
        
        '''
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

    '''Enable the mouse and key action for user interaction.'''
    pygame.event.set_grab(False)  # Allow mouse movement
    pygame.event.set_allowed(pygame.MOUSEMOTION)      # Allow mouse movement
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)  # Allow mouse click
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)    # Optional: allow mouse release
    pygame.event.set_allowed(pygame.KEYDOWN)          # Allow key presses
    pygame.event.set_allowed(pygame.KEYUP)            # Optional: allow key releases

# funct for lock the screen
def deactivate_motion():

    '''Enable the mouse and key action.'''
    pygame.event.set_blocked(pygame.MOUSEMOTION)      # Ignore mouse movement
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)  # Ignore mouse click
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)    # Optional: ignore mouse release
    pygame.event.set_blocked(pygame.KEYDOWN)          # Ignore key presses
    pygame.event.set_blocked(pygame.KEYUP) 

# func to swtich the screen
def screen_switch(screen, frame, size, pos, color_filled, index = 0, speed=0.025):

    '''
    Switch the display/screen with another, can be used to animation
    If the argument 'index' and 'speed' aren't passed in, the default value is used 

    Param:
        screen: display object created by using pygame
            locate the current screen
        frame: list
            the array that contains the different frames that enable the animation
        size: tuple
            (width, height), used to resize the current frame 
        pos: tuple
            (x,y), used to locate the display of frame on the screen
        color_filled: tuple
            (r,g,b), used to decided the background color
        index: int
            used to update the index of frame
        speed: int
            the speed to switch the frame
    Return: 
        index: int
            keep track of the index, update the value
    '''
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
    '''
    Display the text on the screen

    Param:
        text: str
            the text that want to display on screen
        x: int
            the x value to locate the text, center value
        y: int
            the y value to locate the text, center value
        color: tuple
            (r,g,b), the text color
        font: object created by pygame.font.Font
            define the font of text
        screen: display object created by using pygame
            locate the current screen
    Return:
        rect: object created by get_rect
            return the created object that located with the text
    '''
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)
    return rect

