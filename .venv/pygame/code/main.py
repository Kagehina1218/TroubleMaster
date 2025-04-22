# code/main.py
import pygame
import sys
import os
from settings import WIDTH, HEIGHT, FPS, text_intro, BLACK, TEXT_COLOR
from ui import StartScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Start Screen")

    # Initialize start screen
    start_screen = StartScreen(screen)

    font = pygame.font.Font(r'..\assets\font\Grand9K Pixel.ttf', 23)

    running = True
    state = "start_screen"
    index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start screen handling
            if state == "start_screen":
                result = start_screen.handle_event(event)
                if result == "started":
                    state = "intro_text"
                    pygame.display.set_caption("Game Running")

            # Intro text handling
            elif state == "intro_text":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    index += 1
                    if index >= len(text_intro):
                        state = "gameplay"  

        # Drawing section
        screen.fill(BLACK)

        if state == "start_screen":
            start_screen.update()
            start_screen.draw()

        elif state == "intro_text" and index < len(text_intro):
            text = font.render(text_intro[index], True, TEXT_COLOR)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)

        elif state == "gameplay":
            # Placeholder for next part of the game
            pass

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
