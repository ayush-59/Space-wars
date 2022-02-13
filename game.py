import pygame
import os
from assets import *
pygame.font.init()
pygame.mixer.init()


def draw_window(surface, yellow, red, yellow_bullets, red_bullets, yellow_health, red_health):
    surface.blit(SPACE, (0,0))
    pygame.draw.rect(surface, BLACK, BORDER)
    yellow_health_text = HEALTH_TEXT.render("YELLOW HEALTH: " + str(yellow_health), 1, WHITE)
    red_health_text = HEALTH_TEXT.render("RED HEALTH: " + str(red_health), 1, WHITE)
    surface.blit(yellow_health_text, (10, 10))
    surface.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    surface.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    surface.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(surface, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(surface, RED, bullet)

    pygame.display.update()

def yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x-=VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #Right
        yellow.x+=VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0: #Top
        yellow.y-=VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: #Bottom
        yellow.y+=VEL

def red_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x-=VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #Right
        red.x+=VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0: #Top
        red.y-=VEL
    if key_pressed[pygame.K_DOWN] and red.y + red.height + VEL < HEIGHT: #Bottom
        red.y+=VEL

def handle_bullets(yellow, red, yellow_bullets, red_bullets):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
    for bullet1 in yellow_bullets:
        for bullet2 in red_bullets:
            if bullet1.colliderect(bullet2):
                yellow_bullets.remove(bullet1)
                red_bullets.remove(bullet2)
                break

def draw_winner(surface, text):
    winner_text = WINNER_TEXT.render(str(text), 1, WHITE)
    surface.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)

def START():
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("First Game!")
    run = True
    red_health = 5
    yellow_health = 5
    clock = pygame.time.Clock()
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - BULLET_HEIGHT // 2 - 4, BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - BULLET_HEIGHT // 2 - 4, BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

        winner_msg = ""

        if yellow_health == 0:
            winner_msg = "Red Wins!"

        if red_health == 0:
            winner_msg = "Yellow Wins!"

        if winner_msg != "":
            draw_winner(WIN, winner_msg)
            run = False

        key_pressed = pygame.key.get_pressed()

        red_movement(key_pressed, red)
        yellow_movement(key_pressed, yellow)
        handle_bullets(yellow, red, yellow_bullets, red_bullets)

        draw_window(WIN, yellow, red, yellow_bullets, red_bullets, yellow_health, red_health)




if __name__ == "__main__":
    START()
