import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((124, 124, 124))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (160, 180), 30)
circle(screen, (255, 0, 0), (240, 170), 20)
circle(screen, (0, 0, 0), (160, 180), 10)
circle(screen, (0, 0, 0), (240, 170), 7)

polygon(screen, (0, 0, 0), [(200, 180), (206, 174), (116, 83), (110, 90)])
polygon(screen, (0, 0, 0), [(220, 160), (300, 120), (295, 115), (215, 155)])
polygon(screen, (0, 0, 0), [(150, 240), (250, 240), (250, 260), (150, 260)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()