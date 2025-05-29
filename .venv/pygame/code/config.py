import pygame

## CONSTANT
WIDTH = 450
HEIGHT = 800
FPS = 60
WHITE, BLACK = (255,255,255), (0,0,0)
TEXT_COLOR = (255,255,255)
PINK = (245,211,223)
BLUE = (128,178,255)
YES = "YES!!"
CONT = 'CONTINUE ->'
DONE = 'DONE ->'
HI = 'hi :)'
BOTTOM = 675
P_BUT_WIDTH = 100
P_BUT_HEIGHT = 30

COUNT = 1
POS = 0

black_screen = pygame.Surface((WIDTH, HEIGHT))
black_screen_y = 0

## INITIALIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

## DISPLAY TEXT
# Intro text
text_intro = [
    "You're an ordinary office worker.",
    "Just another normal evening now.",
    "You've had such a long, tiring day.",
    "Dreaming of your little cozy home...",
    "Get back home right now?"
]

# Character intro text
text_0 = ["OAO", 
          "What in the world is happening?",
          "Why is my room like this!!????",] 
text_1 = ["NO!!",
          "My favarite vase!",
          "Who could have done this?"]
text_2 = ["Only one truth prevails ...", 
          'and the real offender is...', 'AN AN!!']

texts = [text_0, text_1]
