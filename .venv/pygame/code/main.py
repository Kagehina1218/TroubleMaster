# code/main.py
import pygame
import sys
import os
from ui import StartScreen, Button, IntroAnimation
import config as c
import assets as a

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Start Screen")

    # Initialize
    font = pygame.font.Font(a.font_address, 23)

    frames = [
        pygame.transform.scale(a.img_1, (c.WIDTH,c.HEIGHT)),
        pygame.transform.scale(a.img_2, (c.WIDTH,c.HEIGHT)),
    ]

    start_screen = StartScreen(screen, frames)
    but_1 = Button(screen, 150, 450, a.button_1)
    introAnimate = IntroAnimation(screen)

    running = True
    state = "start_screen"
    index = 0

    while running:
        ## Handle the event
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
                    if index >= len(c.text_intro):
                         state = "intro_but"  
            
            elif state == 'intro_but':
                # change to use with Button class
                result = but_1.handle_event(event)
                if result == "clicked":
                    state = "intro_text_display"
                    pygame.display.set_caption("Game Running")
                # if click on the button -> direct to intro_text_display

            elif state == 'intro_text_display':
                current_text = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if show_text:
                            text_index += 1
                        if text_index >= len(c.texts[current_text]):
                            text_index = 0
                            show_text = False

        ## Out of the for loop
        # Drawing section
        screen.fill(c.BLACK)

        if state == "start_screen":
            start_screen.update()
            start_screen.draw()

        elif state == "intro_text" and index < len(c.text_intro):
            text = font.render(c.text_intro[index], True, c.WHITE)
            text_rect = text.get_rect(center=(c.WIDTH//2, c.HEIGHT//2))
            screen.blit(text, text_rect)

        elif state == "intro_but":
            text = font.render(c.text_intro[-1], True, c.WHITE)
            text_rect = text.get_rect(center=(c.WIDTH//2, c.HEIGHT//2))
            screen.blit(text, text_rect)

            but_1.draw()
            text = font.render(c.YES, True, c.WHITE)
            text_rect = text.get_rect(center=(c.WIDTH//2, 500))
            screen.blit(text, text_rect)
            
        elif state == 'enter_home':
            # Draw the background
            screen.blit(a.bad_living, (0, 0))
            if black_screen_y > -800:
            # Draw the black screen
                c.black_screen.fill(c.BLACK)
                black_screen_y -= 20
                screen.blit(c.black_screen, (0, c.black_screen_y))
            else:
                state = "intro_event" # previously named gameplay
        
        elif state == 'intro_event':
            pass

        elif state == 'intro_char':
            # for character intro that later implemented
            pass

        pygame.display.flip()
        clock.tick(c.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
