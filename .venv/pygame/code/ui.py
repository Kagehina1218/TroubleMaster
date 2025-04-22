import pygame
import os
from settings import HEIGHT, WIDTH

class StartScreen:
    def __init__(self, screen):
        self.screen = screen

        # Load address
        img_1 = pygame.image.load(r'..\assets\screen\start_1.png')
        img_2 = pygame.image.load(r'..\assets\screen\start_2.png')

        # Load animated frames
        self.frames = [
            pygame.transform.scale(img_1, (WIDTH,HEIGHT)),
            pygame.transform.scale(img_2, (WIDTH,HEIGHT)),
        ]
        
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