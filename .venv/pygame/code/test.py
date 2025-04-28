# Import & Setup
import pygame
import sys
from settings import HEIGHT, WIDTH, FPS, BLACK, TEXT_COLOR

BOTTOM = 675

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill('White')
pygame.display.set_caption("Start Screen")
clock = pygame.time.Clock()

pygame.mouse.set_visible(True)
font = pygame.font.Font(r'.venv\pygame\assets\font\Grand9K Pixel.ttf', 23)

# functions
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
# Load living room background
bad_living = pygame.image.load(r'.venv\pygame\assets\screen\bad_living_room.png').convert_alpha()
bad_living = pygame.transform.scale(bad_living, (1350, 675))

# Load shiba inu images
shiba_walk_1 = pygame.image.load(r'.venv\pygame\assets\screen\shiba_inu_walk1.PNG').convert_alpha()
shiba_walk_2 = pygame.image.load(r'.venv\pygame\assets\screen\shiba_inu_walk2.PNG').convert_alpha()
shiba_walk_3 = pygame.image.load(r'.venv\pygame\assets\screen\shiba_inu_walk3.PNG').convert_alpha()
shiba_walk_4 = pygame.image.load(r'.venv\pygame\assets\screen\shiba_inu_walk4.PNG').convert_alpha()
shiba_walk_1 = pygame.transform.scale(shiba_walk_1, (150, 150))
shiba_walk_2 = pygame.transform.scale(shiba_walk_2, (150, 150))
shiba_walk_3 = pygame.transform.scale(shiba_walk_3, (150, 150))
shiba_walk_4 = pygame.transform.scale(shiba_walk_4, (150, 150))
shiba_face_front_1 = pygame.image.load(r'.venv\pygame\assets\screen\shiba_inu_face_forward1.PNG').convert_alpha()
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
state = "enter_home"

# Event
INTRO_EVENT = pygame.USEREVENT + 1

# texts
text_index = 0
current_text = 0
show_text = True

text_0 = ["OAO", 
          "What in the world is happening?",
          "Why is my room like this!!????",] 
text_1 = ["NO!!",
          "My favarite vase!",
          "Who could have done this?"]
texts = [text_0, text_1]

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
                print("Left click detected!")

        
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
        screen.fill(BLACK)  # Clear the screen
        screen.blit(bad_living, (0, 0), camera_rect)

        display_text_block(["Use left and right arrow keys", "to look around."])
        
        if camera_x >= 580:
            if not triggered:
                show_text = True
                current_text = 1
                lock = True # temporarily lock camera movement    
                pygame.time.set_timer(INTRO_EVENT, 5000) # Set a timer for 5 seconds
            
                triggered = True

        if event.type == INTRO_EVENT:
            deactivate_motion()
            # Reset the timer and unlock camera movement
            if shiba_x - camera_x > 300:
                shiba_x -= 2
                print(shiba_x - camera_x)
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
                    print("2 seconds have passed!")
                    pygame.time.set_timer(INTRO_EVENT, 0) # Stop the timer / escape the event
                           
        # shiba_animation()
        # shiba_rect = shiba_surface.get_rect(topleft=(shiba_x - camera_x, shiba_y)) # Update shiba position
        # screen.blit(shiba_surface, shiba_rect) # Draw the shiba inu
       
            

    if show_text and text_index < len(texts[current_text]):
        message = texts[current_text][text_index]
        text_surf = font.render(message, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(WIDTH//2, 650))  # Top-center

        # Transparent black background box
        bg_surf = pygame.Surface((text_rect.width + 30, text_rect.height + 20), pygame.SRCALPHA)
        bg_surf.fill((0, 0, 0, 150))  # semi-transparent black
        screen.blit(bg_surf, text_rect.move(-15, -10))  # Offset for padding
        screen.blit(text_surf, text_rect)     

    if state == "enter_home":
        # Draw the background
        screen.blit(bad_living, (0, 0))
        
        if black_screen_y > -800:
            # Draw the black screen
            black_screen.fill(BLACK)
            black_screen_y -= 20
            screen.blit(black_screen, (0, black_screen_y))
        else:
            state = "gameplay"
        
    pygame.display.flip()
   
    clock.tick(FPS)





