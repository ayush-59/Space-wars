import pygame
import os
from game import *
from button import *
pygame.init()

WHITE = (255, 255, 255)
WIDTH, HEIGHT = 900, 600
SKYBLUE = (0, 0, 100)
DARKBLUE = (0, 0, 255)
GREEN = (0, 255, 0)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')), (WIDTH, HEIGHT))

def Menu():

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MENU")
    b1 = Button(WIDTH // 2 - 200, 100, 400, 80, SKYBLUE, "START")
    b2 = Button(WIDTH // 2 - 200, 200, 400, 80, SKYBLUE, "SINGLE PLAYER")
    b3 = Button(WIDTH // 2 - 200, 300, 400, 80, SKYBLUE, "MULTI PLAYER")
    buttons = [b1, b2, b3]
    run = True
    while run:
        WIN.blit(SPACE, (0, 0))
        for b in buttons:
            b.draw_button(WIN, GREEN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in buttons[:1]:
                    if b.is_over(pos):
                        eval(str(b.text) + "()")


            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.is_over(pos):
                        b.color = DARKBLUE
                    else:
                        b.color = SKYBLUE

    pygame.quit()


if __name__ == "__main__":
    menu()
