import pygame
import menu
pygame.font.init()
from assets import *

SPACESHIP_WIDTH += 20
SPACESHIP_HEIGHT += 20

LOGO = INTRO_TEXT.render('SPACE WARS', 1 , SILVER)
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 180)

def draw_window(surface, yellow, red):
    surface.blit(SPACE, (0, 0))
    surface.blit(LOGO, (WIDTH // 2 - LOGO.get_width() // 2, HEIGHT // 2 - LOGO.get_height() // 2))
    surface.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    surface.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

GAP = 50
LOWER_PATH = HEIGHT // 2 + LOGO.get_height() // 2 + GAP
UPPER_PATH = HEIGHT // 2 - LOGO.get_height() // 2 - GAP - SPACESHIP_HEIGHT
SIDE_PATH = WIDTH // 2 + LOGO.get_width() // 2 + GAP + SPACESHIP_WIDTH

LOWER_PATH = (LOWER_PATH // VEL) * VEL
UPPER_PATH = (UPPER_PATH // VEL) * VEL
SIDE_PATH = (SIDE_PATH // VEL) * VEL

def move_spaceship(yellow, red):
    global YELLOW_SPACESHIP
    global RED_SPACESHIP

    if yellow.x < SIDE_PATH and yellow.y == LOWER_PATH:
        yellow.x += VEL
    elif yellow.x == SIDE_PATH and yellow.y == LOWER_PATH:
        YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)
        yellow.y -= VEL
    elif yellow.x == SIDE_PATH and yellow.y > UPPER_PATH:
        yellow.y -= VEL
    elif yellow.x == SIDE_PATH and yellow.y == UPPER_PATH:
        YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)
        yellow.x -= VEL
    elif yellow.x < SIDE_PATH and yellow.y == UPPER_PATH:
        yellow.x -= VEL


    if red.x < SIDE_PATH and red.y == LOWER_PATH:
        red.x += VEL
    elif red.x == SIDE_PATH and red.y == LOWER_PATH:
        RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)
        red.y -= VEL
    elif red.x == SIDE_PATH and red.y > UPPER_PATH:
        red.y -= VEL
    elif red.x == SIDE_PATH and red.y == UPPER_PATH:
        RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)
        red.x -= VEL
    elif red.x < SIDE_PATH and red.y == UPPER_PATH:
        red.x -= VEL

def intro():
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    yellow = pygame.Rect(0, LOWER_PATH, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(SPACESHIP_WIDTH + 200, LOWER_PATH, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True

    while run:
        clock.tick(FPS)
        draw_window(WIN, yellow, red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        move_spaceship(yellow, red)

        if yellow.x == 0 and yellow.y == UPPER_PATH:
            run = False


    menu.Menu()

if __name__ == "__main__":
    intro()
