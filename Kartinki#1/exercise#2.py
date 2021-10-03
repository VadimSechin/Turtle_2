import pygame
from pygame.draw import *

pygame.init()
import numpy as np

FPS = 30
screen = pygame.display.set_mode((600, 800))
polygon(screen, (0, 150, 200), [(0, 0), (600, 0), (600, 100), (0, 100)])
x1 = 0;
y1 = 100
x2 = 600;
y2 = 450
N = 15
color = (0, 0, 0)
rect(screen, (170, 170, 0), (x1, y1, x2 - x1, y2 - y1))
h = (x2 - x1) / (N + 1)
for i in range(N + 1):
    line(screen, (0, 0, 0), (x1, y1), (x1, y2))
    x1 = x1 + h
polygon(screen, (70, 230, 150), [(0, 451), (600, 451), (600, 800), (0, 800)])
polygon(screen, (0, 0, 0), [(440, 555), (440, 455), (500, 395), (540, 375), (580, 455), (580, 535), (545, 615)])
polygon(screen, (200, 200, 0), [(441, 554), (441, 454), (544, 494), (544, 613)])
polygon(screen, (220, 220, 0), [(443, 453), (501, 394), (544, 492)])
polygon(screen, (220, 220, 0), [(540, 376), (503, 394), (546, 492), (578, 454)])
polygon(screen, (200, 200, 0), [(546, 495), (579, 457), (579, 533), (545, 613)])
ellipse(screen, (0, 0, 0), (462, 500, 55, 60))
ellipse(screen, (0, 0, 0), (455, 550, 20, 10), 1)
ellipse(screen, (0, 0, 0), (437, 570, 25, 20), 1)
ellipse(screen, (0, 0, 0), (447, 553, 20, 25), 1)
ellipse(screen, (110, 110, 110), (448, 554, 18, 23))
ellipse(screen, (0, 0, 0), (427, 587, 25, 10), 1)
ellipse(screen, (0, 0, 0), (422, 592, 13, 13), 1)
ellipse(screen, (0, 0, 0), (400, 597, 30, 10), 1)
ellipse(screen, (0, 0, 0), (388, 600, 20, 10), 1)
ellipse(screen, (0, 0, 0), (368, 600, 30, 5), 1)
ellipse(screen, (0, 0, 0), (361, 597, 12, 15), 1)
ellipse(screen, (0, 0, 0), (350, 605, 18, 8), 1)
ellipse(screen, (0, 0, 0), (340, 611, 17, 10), 1)

ellipse(screen, (110, 110, 110), (290, 600, 35, 40))
ellipse(screen, (110, 110, 110), (317, 625, 9, 35))
ellipse(screen, (110, 110, 110), (300, 657, 25, 12))
ellipse(screen, (110, 110, 110), (250, 580, 65, 45))
ellipse(screen, (110, 110, 110), (243, 580, 30, 40))
ellipse(screen, (110, 110, 110), (167, 582, 100, 70))
ellipse(screen, (110, 110, 110), (262, 620, 13, 35))
ellipse(screen, (110, 110, 110), (252, 650, 22, 10))
ellipse(screen, (110, 110, 110), (209, 643, 30, 60))
ellipse(screen, (110, 110, 110), (200, 698, 27, 15))
ellipse(screen, (110, 110, 110), (150, 605, 30, 70))
ellipse(screen, (110, 110, 110), (141, 668, 27, 15))
polygon(screen, (0, 0, 0), [(160, 620), (230, 620), (230, 550), (160, 550)])
polygon(screen, (110, 110, 110), [(162, 618), (228, 618), (228, 552), (162, 552)])
ellipse(screen, (0, 0, 0), (151, 548, 20, 30))
ellipse(screen, (110, 110, 110), (153, 550, 16, 26))
ellipse(screen, (0, 0, 0), (221, 548, 20, 30))
ellipse(screen, (110, 110, 110), (223, 550, 16, 26))
ellipse(screen, (255, 255, 255), (175, 572, 15, 5))
ellipse(screen, (255, 255, 255), (200, 572, 15, 5))
ellipse(screen, (0, 0, 0), (205, 572, 6, 6))
ellipse(screen, (0, 0, 0), (180, 572, 6, 6))

polygon(screen, (255, 255, 255), [(180, 602), (183, 592), (185, 598)])
polygon(screen, (255, 255, 255), [(207, 602), (202, 598), (204, 592)])
arc(screen, (0, 0, 0), (175, 600, 40, 20), 0, np.pi)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()