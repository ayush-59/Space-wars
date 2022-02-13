import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT=900,600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SILVER = (184, 194, 187)

BORDER=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

FPS = 60
VEL = 5
BULLET_VEL = 7


SPACESHIP_HEIGHT,SPACESHIP_WIDTH=50,40
BULLET_WIDTH, BULLET_HEIGHT = 8, 4

red_bullets = []
yellow_bullets = []
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')), (WIDTH, HEIGHT))

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.ogg'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.ogg'))

INTRO_TEXT = pygame.font.SysFont('comicsans', 80)
HEALTH_TEXT = pygame.font.SysFont('comicsans', 40)
WINNER_TEXT = pygame.font.SysFont('comicsans', 100)
