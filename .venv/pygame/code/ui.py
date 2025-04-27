import pygame
import os

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


class Button():
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