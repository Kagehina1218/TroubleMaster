# Loading of images, fonts, sounds
import pygame
import config as c

## FONT LOAD
font_address = r'..\assets\font\Grand9K Pixel.ttf'

## MUSIC LOAD
background_music = r'..\assets\music\BACKGROUND-pixabay-happy-flowers-playful-cute-xylophone-187119.mp3'
sus_music = r'..\assets\music\SUS-pixabay-cartoon-music-animation-video-funny-cute-quirky-background-intro-255037.mp3'
click_music = r'..\assets\music\BUTTON-CLICK-mixkit-game-ball-tap-2073.wav'

## IMAGE LOAD
# Start screen
start_screen_1 = pygame.image.load(r'..\assets\screen\start_1.png')
start_screen_2 = pygame.image.load(r'..\assets\screen\start_2.png')
start_screen_1 = pygame.transform.scale(start_screen_1, (c.WIDTH, c.HEIGHT))
start_screen_2 = pygame.transform.scale(start_screen_2, (c.WIDTH, c.HEIGHT))

img_1 = pygame.image.load(r'..\assets\screen\start_1.png')
img_2 = pygame.image.load(r'..\assets\screen\start_2.png')

# Button
but = pygame.image.load(r'..\assets\screen\button.png')
button_1 = pygame.transform.scale(but, ((c.WIDTH/3, c.HEIGHT/8)))

# Yes button
yes_button = pygame.image.load(r'..\assets\screen\button.png').convert_alpha()
yes_button = pygame.transform.scale(yes_button, (c.WIDTH/3, c.HEIGHT/8))
yes_button_rect = yes_button.get_rect(center=(c.WIDTH//2, c.HEIGHT//2))

# Bad living room
bad_living = pygame.image.load(r'..\assets\screen\bad_living_room.png').convert_alpha()
bad_living = pygame.transform.scale(bad_living, (1350, 675))

# Shiba animation
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
shiba_surface = shiba_walk[0]
shiba_shadow = pygame.Surface((100, 20), pygame.SRCALPHA)
pygame.draw.ellipse(shiba_shadow, (0, 0, 0, 100), shiba_shadow.get_rect())

# Profile images
profile_back = pygame.image.load(r'..\assets\screen\profile_back.png').convert_alpha()
profile_back= pygame.transform.scale(profile_back, (c.WIDTH, c.HEIGHT))

white_cat = pygame.image.load(r'..\assets\profile\white.png').convert_alpha()
white_cat = pygame.transform.scale(white_cat, (140, 150))

black_cat = pygame.image.load(r'..\assets\profile\black.png').convert_alpha()
black_cat = pygame.transform.scale(black_cat, (140, 150))

orange_cat = pygame.image.load(r'..\assets\profile\orange.png').convert_alpha()
orange_cat = pygame.transform.scale(orange_cat, (140, 150))

shiba = pygame.image.load(r'..\assets\profile\chai.png').convert_alpha()
shiba = pygame.transform.scale(shiba, (140, 150))

husky = pygame.image.load(r'..\assets\profile\ha.png').convert_alpha()
husky = pygame.transform.scale(husky, (140, 150))

parrot = pygame.image.load(r'..\assets\profile\yingwu.png').convert_alpha()
parrot = pygame.transform.scale(parrot, (140, 150))

# Caught 
white_cat_c = pygame.image.load(r'..\assets\profile\white_c.png').convert_alpha()
white_cat_c = pygame.transform.scale(white_cat_c, (140, 150))

black_cat_c = pygame.image.load(r'..\assets\profile\black_c.png').convert_alpha()
black_cat_c = pygame.transform.scale(black_cat_c, (140, 150))

orange_cat_c = pygame.image.load(r'..\assets\profile\orange_c.png').convert_alpha()
orange_cat_c = pygame.transform.scale(orange_cat_c, (140, 150))

shiba_c = pygame.image.load(r'..\assets\profile\chai_c.png').convert_alpha()
shiba_c = pygame.transform.scale(shiba_c, (140, 150))

husky_c = pygame.image.load(r'..\assets\profile\ha_c.png').convert_alpha()
husky_c = pygame.transform.scale(husky_c, (140, 150))

parrot_c = pygame.image.load(r'..\assets\profile\yingwu_c.png').convert_alpha()
parrot_c = pygame.transform.scale(parrot_c, (140, 150))

white_find = [white_cat, white_cat_c]
black_find = [black_cat, black_cat_c]
orange_find = [orange_cat, orange_cat_c]
shiba_find = [shiba, shiba_c]
husky_find = [husky, husky_c]
parrot_find = [parrot, parrot_c]

# Profile button to switch to next screen 
cont_button = pygame.transform.scale(but, (c.WIDTH/3, c.HEIGHT/8))
cont_button_rect = cont_button.get_rect(center=(c.WIDTH//2, c.HEIGHT//2))

# Button to back to profile screen
back_but = pygame.transform.scale(but, (c.P_BUT_WIDTH*1.5, c.P_BUT_HEIGHT*1.5))
back_rect = back_but.get_rect(center=(c.WIDTH/2, c.HEIGHT/1.25))

# Profile button to know more
white_know_but = pygame.transform.scale(but, (c.P_BUT_WIDTH, c.P_BUT_HEIGHT))
white_know_rect = white_know_but.get_rect(topleft=(27, 340))

black_know_but = pygame.transform.scale(but, (c.P_BUT_WIDTH, c.P_BUT_HEIGHT))
black_know_rect = black_know_but.get_rect(topleft=(174, 340))

orange_know_but = pygame.transform.scale(but, (c.P_BUT_WIDTH, c.P_BUT_HEIGHT))
orange_know_rect = orange_know_but.get_rect(topleft=(321, 340))

shiba_know_but = pygame.transform.scale(but, (c.P_BUT_WIDTH, c.P_BUT_HEIGHT))
shiba_know_rect = shiba_know_but.get_rect(topleft=(27, 710))

husky_know_but = pygame.transform.scale(but, (c.P_BUT_WIDTH, c.P_BUT_HEIGHT))
husky_know_rect = husky_know_but.get_rect(topleft=(174, 710))

parrots_know_but = pygame.transform.scale(but, (c.P_BUT_WIDTH, c.P_BUT_HEIGHT))
parrots_know_rect = parrots_know_but.get_rect(topleft=(321, 710))

# Profile animation image
white_a1 = pygame.image.load(r'..\assets\profile_a\white_a1.PNG').convert_alpha()
white_a2 = pygame.image.load(r'..\assets\profile_a\white_a2.PNG').convert_alpha()
whites = [white_a1, white_a2]
whites_index = 0

black_a1 = pygame.image.load(r'..\assets\profile_a\black_a1.PNG').convert_alpha()
black_a2 = pygame.image.load(r'..\assets\profile_a\black_a2.PNG').convert_alpha()
blacks = [black_a1, black_a2]
blacks_index = 0

orange_a1 = pygame.image.load(r'..\assets\profile_a\orange_a1.PNG').convert_alpha()
orange_a2 = pygame.image.load(r'..\assets\profile_a\orange_a2.PNG').convert_alpha()
oranges = [orange_a1, orange_a2]
oranges_index = 0

shiba_a1 = pygame.image.load(r'..\assets\profile_a\shiba_a1.PNG').convert_alpha()
shiba_a2 = pygame.image.load(r'..\assets\profile_a\shiba_a2.PNG').convert_alpha()
shibas = [shiba_a1, shiba_a2]
shibas_index = 0

husky_a1 = pygame.image.load(r'..\assets\profile_a\husky_a1.PNG').convert_alpha()
husky_a2 = pygame.image.load(r'..\assets\profile_a\husky_a2.PNG').convert_alpha()
huskys = [husky_a1, husky_a2]
huskys_index = 0

parrots_a1 = pygame.image.load(r'..\assets\profile_a\parrot_a1.PNG').convert_alpha()
parrots_a2 = pygame.image.load(r'..\assets\profile_a\parrot_a2.PNG').convert_alpha()
parrots = [parrots_a1, parrots_a2]
parrots_index = 0

# Event start
bad_living_1 = pygame.image.load(r'..\assets\event\bad_living_event.png').convert_alpha()
bad_living_1 = pygame.transform.scale(bad_living_1, (1350, 675))

event_1 = pygame.image.load(r'..\assets\event\event_1.png').convert_alpha()
event_1 = pygame.transform.scale(event_1, (1350, 675))

# Done button
done_but = pygame.transform.scale(but, ((c.WIDTH/3, c.HEIGHT/10)))
done_rect = done_but.get_rect(topleft=(0, 0))
