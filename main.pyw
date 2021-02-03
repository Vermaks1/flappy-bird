import pygame
import sys
import random
import os

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 800, 1080
collide = False
collide2 = False


rect_size = w, h = 250, 250
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)

FPS = 120
RED = (255, 0, 0, 180)
BLUE = (0, 0, 255, 180)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)
x = 0
y = 0
block = False
speed_x, speed_y = 5, 4
bird = pygame.image.load('image/bird.png')
bird_rect = bird.get_rect()
print(bird_rect)
colony = pygame.image.load('image/colony.png')
colony_rect = colony.get_rect(topleft=(400,800))
print(colony_rect)
colony1 = pygame.image.load('image/colony1.png')
colony1_rect = colony1.get_rect(topleft=(100,-100))
print(colony1_rect)


pygame.init()
pygame.display.set_caption('Flappy bird')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
font = pygame.font.SysFont('Arial', 24, True, False)
clock = pygame.time.Clock()
bird = pygame.transform.scale(bird,(50,50))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
            e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                bird_rect.y -= 70
    screen.fill(BG)

    bird_rect.y += 2
    colony_rect.x -= 1
    colony1_rect.x -= 1

    screen.blit(bird, bird_rect)
    screen.blit(colony, colony_rect)
    screen.blit(colony1, colony1_rect)
    pygame.display.update()
    clock.tick(FPS)
