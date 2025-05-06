# Import & Setup
import pygame
import sys
from settings import HEIGHT, WIDTH, FPS, BLACK, TEXT_COLOR
import assets as a
import ui
import config as c
import time
from ui import ToggleImage

BOTTOM = 675

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill('White')
pygame.display.set_caption("Start Screen")
clock = pygame.time.Clock()

pygame.mouse.set_visible(True)
font = pygame.font.Font(r'..\assets\font\Grand9K Pixel.ttf', 23)

# functions
def start_animation():
    global start_screen_index, start_screen_surface
    # walking animation
    start_screen_index += 0.025
    if start_screen_index >= len(start_screen):start_screen_index =0
    start_screen_surface = start_screen[int(start_screen_index)]

def shiba_animation():

    # play walking animation
    global shiba_index, shiba_surface
    # walking animation
    shiba_index += 0.1
    if shiba_index >= len(shiba_walk):shiba_index =0
    shiba_surface = shiba_walk[int(shiba_index)]

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

def display_text_block(text_list, theScreen=screen, theFont=font, y_bottom=780, padding=20, alpha=150):
    """
    Displays a list of text lines stacked vertically with a transparent background behind them.
    """
    # Render all text lines and store their surfaces and rects
    text_surfs = [font.render(line, True, (255, 255, 255)) for line in text_list]
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
    bg_rect = bg_surf.get_rect(centerx=screen.get_width() // 2, bottom=y_bottom)

    # Blit background
    screen.blit(bg_surf, bg_rect)

    # Blit each text line
    current_y = bg_rect.top + padding // 2
    for surf, rect in zip(text_surfs, text_rects):
        rect.midtop = (screen.get_width() // 2, current_y)
        screen.blit(surf, rect)
        current_y += rect.height + spacing

################## ==LOAD IMAGE== #################
# Load start screen images
start_screen_1 = pygame.image.load(r'..\assets\screen\start_1.png')
start_screen_2 = pygame.image.load(r'..\assets\screen\start_2.png')
start_screen_1 = pygame.transform.scale(start_screen_1, (WIDTH, HEIGHT))
start_screen_2 = pygame.transform.scale(start_screen_2, (WIDTH, HEIGHT))

start_screen = [start_screen_1, start_screen_2]
start_screen_index = 0

# Load start screen button position
start_button_rect = pygame.Rect(135,325,200,80)

# Load YES! button image
yes_button = pygame.image.load(r'..\assets\screen\button.png').convert_alpha()
yes_button = pygame.transform.scale(yes_button, (WIDTH/3, HEIGHT/8))
yes_button_rect = yes_button.get_rect(center=(WIDTH//2, HEIGHT//2))

# Load living room background
bad_living = pygame.image.load(r'..\assets\screen\bad_living_room.png').convert_alpha()
bad_living = pygame.transform.scale(bad_living, (1350, 675))

# Load shiba inu images
shiba_walk_1 = pygame.image.load(r'..\assets\screen\shiba_inu_walk1.PNG').convert_alpha()
shiba_walk_2 = pygame.image.load(r'..\assets\screen\shiba_inu_walk2.PNG').convert_alpha()
shiba_walk_3 = pygame.image.load(r'..\assets\screen\shiba_inu_walk3.PNG').convert_alpha()
shiba_walk_4 = pygame.image.load(r'..\assets\screen\shiba_inu_walk4.PNG').convert_alpha()
shiba_walk_1 = pygame.transform.scale(shiba_walk_1, (150, 150))
shiba_walk_2 = pygame.transform.scale(shiba_walk_2, (150, 150))
shiba_walk_3 = pygame.transform.scale(shiba_walk_3, (150, 150))
shiba_walk_4 = pygame.transform.scale(shiba_walk_4, (150, 150))
shiba_face_front_1 = pygame.image.load(r'..\assets\screen\shiba_inu_face_forward1.PNG').convert_alpha()
shiba_face_front_1 = pygame.transform.scale(shiba_face_front_1, (150, 150))

shiba_walk = [shiba_walk_1, shiba_walk_2, shiba_walk_3, shiba_walk_4]
shiba_index = 0
shiba_x = 1100
shiba_y = 500

shiba_surface = shiba_walk[shiba_index]
shiba_shadow = pygame.Surface((100, 20), pygame.SRCALPHA)
pygame.draw.ellipse(shiba_shadow, (0, 0, 0, 100), shiba_shadow.get_rect())

# black screen
black_screen = pygame.Surface((WIDTH, HEIGHT))
black_screen_y = 0

# Set up camera
camera_x = 0  # Initial camera position 
camera_y = 0
camera_speed = 5
lock = False

# state
triggered = False
char_intro = False
# state = "start"
# state = "enter_home"
state = 'char_intro'
# state = 'crime_scene_1'
# state = 'event_1'

# Event
INTRO_EVENT = pygame.USEREVENT + 1

# texts
text_index = 0
current_text = 0
show_text = False
w_find = 0
b_find = 0
o_find = 0
s_find = 0
h_find = 0
p_find = 0
chose = None
# pause_ready = False

text_intro = ["You're an ordinary office worker.",
              "Just another normal evening now.",
              "You've had such a long, tiring day.",
              "Dreaming of your little cozy home...",
              "Get back home right now?"]
text_0 = ["OAO", 
          "What in the world is happening?",
          "Why is my room like this!!????",] 
text_1 = ["NO!!",
          "My favarite vase!",
          "Who could have done this?"]
texts = [text_intro, text_0, text_1]
# texts = [text_0, text_1]

white_toggle = ToggleImage((8, 180), a.white_find)
black_toggle = ToggleImage((155, 180), a.black_find)
orange_toggle = ToggleImage((302, 180), a.orange_find)

shiba_toggle = ToggleImage((8, 550), a.shiba_find)
husky_toggle = ToggleImage((155, 550), a.husky_find)
parrot_toggle = ToggleImage((302, 550), a.parrot_find)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if show_text:
                    text_index += 1
                if text_index >= len(texts[current_text]):
                    text_index = 0
                    show_text = False
                    # current_text += 1
                # print("Left click detected!")
                              
        # shiba_animation()
        # shiba_rect = shiba_surface.get_rect(topleft=(shiba_x - camera_x, shiba_y)) # Update shiba position
        # screen.blit(shiba_surface, shiba_rect) # Draw the shiba inu

    if state == "start":
        start_animation()
        screen.blit(start_screen_surface, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                show_text = True
                current_text = 0
                state = "entering_home"
                
    if state == "entering_home":
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()
        if not show_text:
            screen.blit(yes_button, yes_button_rect)
            display_text_block(["YES!!"], y_bottom=425, alpha=0)
            if yes_button_rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    show_text = True
                    current_text = 1
                    state = "entered_home"

    if state == "entered_home":
        # Draw the background
        screen.blit(bad_living, (0, 0))
        
        if black_screen_y > -800:
            # Draw the black screen
            black_screen.fill(BLACK)
            black_screen_y -= 20
            screen.blit(black_screen, (0, black_screen_y))
        else:
            state = "gameplay"

    if state == "gameplay":
        ######### CAMERA MOVEMENT #########
        # Get key presses
        keys = pygame.key.get_pressed()

        # Move camera with arrow keys
        if keys[pygame.K_LEFT] and lock == False:
            if camera_x > 0:
                camera_x -= camera_speed
        if keys[pygame.K_RIGHT]and lock == False:
            if camera_x < 1350-WIDTH:
                camera_x += camera_speed

        # Define camera view (the area of background to show)
        camera_rect = pygame.Rect(camera_x, camera_y, WIDTH, 750)

        # Draw that portion of the background to the screen
        screen.fill(c.BLACK)  # Clear the screen
        screen.blit(bad_living, (0, 0), camera_rect)

        display_text_block(["Use left and right arrow keys", "to look around."])
        
        if camera_x >= 580:
            if not triggered:
                show_text = True
                current_text = 2
                lock = True # temporarily lock camera movement    
                pygame.time.set_timer(INTRO_EVENT, 5000) # Set a timer for 5 seconds
            
                triggered = True

        if event.type == INTRO_EVENT:
            deactivate_motion()
            # Reset the timer and unlock camera movement
            if shiba_x - camera_x > 300:
                shiba_x -= 2
                # print(shiba_x - camera_x)
                shiba_animation()
                shiba_rect = shiba_surface.get_rect(topleft=(shiba_x - camera_x, shiba_y)) # Update shiba position
                screen.blit(shiba_shadow, (shiba_x - camera_x + 25, shiba_y + 135))
                screen.blit(shiba_surface, shiba_rect) # Draw the shiba inu
                
                start_time = pygame.time.get_ticks() # Get the current time in milliseconds

            elif shiba_x - camera_x <= 300:
                shiba_surface = shiba_face_front_1
                screen.blit(shiba_shadow, (shiba_x - camera_x + 25, shiba_y + 135))
                screen.blit(shiba_face_front_1, shiba_rect)
                if pygame.time.get_ticks() - start_time >= 2000: # Check if 2 seconds have passed
                    # print("2 seconds have passed!")
                    pygame.time.set_timer(INTRO_EVENT, 0) # Stop the timer / escape the event
                    state = 'char_pause'

    if state == 'char_pause':
        activate_motion()
        screen.fill(c.BLACK)
        display_text_block(['Time to bring in the suspect ...'])
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            state = 'char_load'
        

    if state == 'char_load':
        screen.blit(a.profile_back, (0, 0))
        if black_screen_y > -800:
            # Draw the black screen
            black_screen.fill(BLACK)
            black_screen_y -= 10
            screen.blit(a.profile_back, (0, black_screen_y))
        else:
            state = "char_intro"

    if state == 'char_intro':
        activate_motion()
        # Text on top
        screen.blit(a.profile_back, (0, black_screen_y))
        display_text_block(["Click CONTINUE to next event."], y_bottom=100)
        # First row
        screen.blit(a.white_cat, (8, 180))
        screen.blit(a.black_cat, (155, 180))
        screen.blit(a.orange_cat, (302, 180))

        # Word displayed within the two rows
        display_text_block(["Want to know more about us? :)", 'Try to click different buttons!!'], y_bottom=500, alpha=100)
        
        # Second row
        screen.blit(a.shiba, (8, 550))
        screen.blit(a.husky, (155, 550))
        screen.blit(a.parrot, (302, 550))

        # Button initialize
        screen.blit(a.white_know_but, a.white_know_rect)
        screen.blit(a.black_know_but, a.black_know_rect)
        screen.blit(a.orange_know_but, a.orange_know_rect)
        screen.blit(a.shiba_know_but, a.shiba_know_rect)
        screen.blit(a.husky_know_but, a.husky_know_rect)
        screen.blit(a.parrots_know_but, a.parrots_know_rect)

        # Continue button to go to next event 
        cont = ui.draw_text(c.CONT, c.WIDTH/2, 140, BLACK, font, screen)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if a.white_know_rect.collidepoint(mouse_pos):
                state = "white_p"
            elif a.black_know_rect.collidepoint(mouse_pos):
                state = "black_p"
            elif a.orange_know_rect.collidepoint(mouse_pos):
                state = "orange_p"
            elif a.shiba_know_rect.collidepoint(mouse_pos):
                state = "shiba_p"
            elif a.husky_know_rect.collidepoint(mouse_pos):
                state = "husky_p"
            elif a.parrots_know_rect.collidepoint(mouse_pos):
                state = "parrots_p"
            elif cont.collidepoint(mouse_pos):
                state = 'event_pause'

    if state ==  'white_p':
        # def screen_switch(screen, frame, size, pos, color_filled, index = 0, speed=0.1):
        a.whites_index = ui.screen_switch(screen, a.whites, (300,300), (75,175), c.PINK, index = a.whites_index)
        display_text_block(["Hi! I am AN AN. "], y_bottom=600)
        screen.blit(a.back_but, a.back_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and state == 'white_p':
            mouse_pos = pygame.mouse.get_pos()
            if a.back_rect.collidepoint(mouse_pos):
                screen.blit(a.profile_back, (0, 0))
                state = "char_intro"

    if state ==  'black_p':
        a.blacks_index = ui.screen_switch(screen, a.blacks, (300,300), (75,175), c.BLUE, index = a.blacks_index)
        display_text_block(["Hi! I am JI JI. "], y_bottom=600)
        screen.blit(a.back_but, a.back_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if a.back_rect.collidepoint(mouse_pos):
                screen.blit(a.profile_back, (0, 0))
                state = "char_intro"

    if state ==  'orange_p':
        a.oranges_index = ui.screen_switch(screen, a.oranges, (300,300), (75,175), c.PINK, index = a.oranges_index)
        display_text_block(["Hi! I am JU JU. "], y_bottom=600)
        screen.blit(a.back_but, a.back_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if a.back_rect.collidepoint(mouse_pos):
                screen.blit(a.profile_back, (0, 0))
                state = "char_intro"

    if state == 'shiba_p':
        a.shibas_index = ui.screen_switch(screen, a.shibas, (300,300), (75,175), c.BLUE, index = a.shibas_index)
        display_text_block(["Hi! I am PI PI. "], y_bottom=600)
        screen.blit(a.back_but, a.back_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if a.back_rect.collidepoint(mouse_pos):
                screen.blit(a.profile_back, (0, 0))
                state = "char_intro"

    if state ==  'husky_p':
        a.huskys_index = ui.screen_switch(screen, a.huskys, (300,300), (75,175), c.PINK, index = a.huskys_index)
        display_text_block(["Hi! I am PING PING."], y_bottom=600)
        screen.blit(a.back_but, a.back_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if a.back_rect.collidepoint(mouse_pos):
                screen.blit(a.profile_back, (0, 0))
                state = "char_intro"
    
    if state ==  'parrots_p':
        a.parrots_index = ui.screen_switch(screen, a.parrots, (300,300), (75,175), c.BLUE, index = a.parrots_index)
        display_text_block(["Hi! I am HI HI. "], y_bottom=600)
        screen.blit(a.back_but, a.back_rect)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if a.back_rect.collidepoint(mouse_pos):
                screen.blit(a.profile_back, (0, 0))
                state = "char_intro"
    
    # have the circle that hightlight the vase
    # clickable -> show the big vase
    if state == 'event_pause':
        activate_motion()
        screen.fill(c.BLACK)
        display_text_block(["Who’s behind this terrible tragedy?", "Time to go back to the crime scene."])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            state = 'crime_scene_overall'


    if state == 'crime_scene_overall':
        keys = pygame.key.get_pressed()
        lock = False
        # Move camera with arrow keys
        if keys[pygame.K_LEFT] and lock == False:
            if camera_x > 0:
                camera_x -= camera_speed
        if keys[pygame.K_RIGHT]and lock == False:
            if camera_x < 1350-WIDTH:
                camera_x += camera_speed

        # Define camera view (the area of background to show)
        camera_rect = pygame.Rect(camera_x, camera_y, WIDTH, 750)

        # Draw that portion of the background to the screen
        screen.fill(c.BLACK)  # Clear the screen
        screen.blit(a.bad_living, (0, 0), camera_rect)

        display_text_block(["Use left and right arrow keys", "to look around."])

        # When user click then scene, replace the screen with bad_living_1 and lock to pos of vase
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            state = 'crime_scene_1'

    if state == 'crime_scene_1':
        keys = pygame.key.get_pressed()

        # Move camera with arrow keys
        if keys[pygame.K_LEFT] and lock == False:
            if camera_x > 0:
                camera_x -= camera_speed
        if keys[pygame.K_RIGHT]and lock == False:
            if camera_x < 1350-WIDTH:
                camera_x += camera_speed

        # Define camera view (the area of background to show)
        camera_rect = pygame.Rect(camera_x, camera_y, WIDTH, 750)

        # Draw that portion of the background to the screen
        screen.fill(c.BLACK)  # Clear the screen
        screen.blit(a.bad_living_1, (0, 0), camera_rect)

        display_text_block(["Use left and right arrow keys", "to look around."])

        if camera_x >= 580:
            lock = True # temporarily lock camera movement    
            event1_rect = pygame.Rect(0,0,c.WIDTH,c.HEIGHT)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if event1_rect.collidepoint(mouse_pos):
                    state = "event_1"


    if state == 'event_1':
        lock = False
        keys = pygame.key.get_pressed()

        # Move camera with arrow keys
        if keys[pygame.K_LEFT] and lock == False:
            if camera_x > 0:
                camera_x -= camera_speed
        if keys[pygame.K_RIGHT]and lock == False:
            if camera_x < 1350-WIDTH:
                camera_x += camera_speed

        # Define camera view (the area of background to show)
        camera_rect = pygame.Rect(camera_x, camera_y, WIDTH, 750)

        # Draw that portion of the background to the screen
        screen.fill(c.BLACK)  # Clear the screen
        screen.blit(a.event_1, (0, 0), camera_rect)

        display_text_block(["Use left and right arrow keys", "to look for evidences."])

        done_rect = pygame.Rect(0,700,c.WIDTH,100)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if done_rect.collidepoint(mouse_pos):
                state = "char_chose"

    if state == 'char_chose':
        screen.blit(a.profile_back, (0, 0))
        # # First row
        # screen.blit(a.white_find[w_find], (8, 180))
        # screen.blit(a.black_find[b_find], (155, 180))
        # screen.blit(a.orange_find[o_find], (302, 180))
        
        # # Word displayed within the two rows
        # display_text_block(["Who do you think is behind all this?","Just one is responsible..."], y_bottom=480, alpha=100)
        
        # # Second row
        # screen.blit(a.shiba_find[s_find], (8, 550))
        # screen.blit(a.husky_find[h_find], (155, 550))
        # screen.blit(a.parrot_find[p_find], (302, 550))

        # rect_w = a.white_find[w_find].get_rect(topleft=(8, 180))
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if rect_w.collidepoint(event.pos):
        #         w_find = 1 - w_find

        all_toggles = [white_toggle, black_toggle, orange_toggle, shiba_toggle, husky_toggle, parrot_toggle]

        for toggle in all_toggles:
            toggle.draw(screen)

        display_text_block(["Who do you think is behind all this?", "Just one is responsible..."], y_bottom=480, alpha=100)
        done = ui.draw_text(c.DONE, c.WIDTH/2, 100, BLACK, font, screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if done.collidepoint(mouse_pos) and event.button == 1:
                state = 'event_1_result'

            for toggle in all_toggles:
                toggle.handle_click(event.pos)

    if state == 'event_1_result':
        screen.fill(BLACK)
        display_text_block(["Only one truth prevails ...", 'and the real culprit is -'])
        event1_rect = pygame.Rect(0,0,c.WIDTH,c.HEIGHT)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if event1_rect.collidepoint(mouse_pos):
                screen.fill(BLACK)
                display_text_block(["AN AN"])


    
    if show_text and text_index < len(texts[current_text]):
        message = texts[current_text][text_index]
        text_surf = font.render(message, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(WIDTH//2, 650))  # Top-center

        # Transparent black background box
        bg_surf = pygame.Surface((text_rect.width + 30, text_rect.height + 20), pygame.SRCALPHA)
        bg_surf.fill((0, 0, 0, 150))  # semi-transparent black
        screen.blit(bg_surf, text_rect.move(-15, -10))  # Offset for padding
        screen.blit(text_surf, text_rect)   

    pygame.display.flip()
   
    clock.tick(FPS)