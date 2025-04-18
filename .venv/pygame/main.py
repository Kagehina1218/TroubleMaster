# Initialize Pygame
# Loads setting and seets
# Main game loop
# Handle game states (menu)
import pygame

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(())
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()