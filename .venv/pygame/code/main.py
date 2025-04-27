# code/main.py
import pygame
import sys
import os
from ui import StartScreen, Button

# Variables
WIDTH = 450
HEIGHT = 800
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
YES = "YES!!"

text_intro = [
    "You're an ordinary office worker.",
    "Just another normal evening now.",
    "You've had such a long, tiring day.",
    "Dreaming of your little cozy home...",
    "Get back home right now?"
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Start Screen")

    # Initialize
    img_1 = pygame.image.load(r'..\assets\screen\start_1.png')
    img_2 = pygame.image.load(r'..\assets\screen\start_2.png')
    font = pygame.font.Font(r'..\assets\font\Grand9K Pixel.ttf', 23)

    button_1 = pygame.image.load(r'..\assets\screen\button.png')
    button_1 = pygame.transform.scale(button_1, ((WIDTH/3,HEIGHT/8)))

    frames = [
        pygame.transform.scale(img_1, (WIDTH,HEIGHT)),
        pygame.transform.scale(img_2, (WIDTH,HEIGHT)),
    ]

    start_screen = StartScreen(screen, frames)
    but_1 = Button(screen, 150, 450, button_1)

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
            text = font.render(text_intro[index], True, WHITE)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)

        elif state == "gameplay":
            text = font.render(text_intro[-1], True, WHITE)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)

            but_1.draw()
            text = font.render(YES, True, WHITE)
            text_rect = text.get_rect(center=(WIDTH//2, 500))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
