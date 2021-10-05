import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))


def fence(x, y, a, b, n, color):
    """
    функция рисует эабор на экране.
    :param color: параметр, отвечающий за цвт забора
    :param x: x-вая координата верхнего левого угла забора
    :param y: y:-вая координата верхнего левого угла забора
    :param a: ширина забора
    :param b: выстора забора
    :param n: число, отвечающее за количество досок в заборе
    """
    rect(screen, (color), (x, y, a, b))
    h = a / n
    for i in range(n + 1):
        line(screen, (0, 0, 0), (x, y), (x, y + b))
        x = x + h


def dog(x, y, a, color):
    """
    функция рисует собау на экране
    :param color: параметр, отвечающий за цвет тела собаки
    :param x: параметр, отвечающий за положение собоаки пр координате x
    :param y: параметр, отвечающий за положение собоаки пр координате y
    :param a: коеффицент гомотетии для собаки. Если a>0, то собака просто увеличивается в размерх.
    Если a<0, то собака переворачивается на 180 градусов и увеличивается в модуль a раз
    """
    ellipse(screen, color,
            (x + 290 * a - (np.abs(a) - a) * 35 / 2, y + 600 * np.abs(a), 35 * np.abs(a), 40 * np.abs(a)))
    ellipse(screen, color,
            (x + 317 * a - (np.abs(a) - a) * 9 / 2, y + 625 * np.abs(a), 9 * np.abs(a), 35 * np.abs(a)))
    ellipse(screen, color,
            (x + 300 * a - (np.abs(a) - a) * 25 / 2, y + 657 * np.abs(a), 25 * np.abs(a), 12 * np.abs(a)))
    ellipse(screen, color,
            (x + 250 * a - (np.abs(a) - a) * 65 / 2, y + 580 * np.abs(a), 65 * np.abs(a), 45 * np.abs(a)))
    ellipse(screen, color,
            (x + 243 * a - (np.abs(a) - a) * 30 / 2, y + 580 * np.abs(a), 30 * np.abs(a), 40 * np.abs(a)))
    ellipse(screen, color,
            (x + 167 * a - (np.abs(a) - a) * 100 / 2, y + 582 * np.abs(a), 100 * np.abs(a), 70 * np.abs(a)))
    ellipse(screen, color,
            (x + 262 * a - (np.abs(a) - a) * 13 / 2, y + 620 * np.abs(a), 13 * np.abs(a), 35 * np.abs(a)))
    ellipse(screen, color,
            (x + 252 * a - (np.abs(a) - a) * 22 / 2, y + 650 * np.abs(a), 22 * np.abs(a), 10 * np.abs(a)))
    ellipse(screen, color,
            (x + 209 * a - (np.abs(a) - a) * 30 / 2, y + 643 * np.abs(a), 30 * np.abs(a), 60 * np.abs(a)))
    ellipse(screen, color,
            (x + 200 * a - (np.abs(a) - a) * 27 / 2, y + 698 * np.abs(a), 27 * np.abs(a), 15 * np.abs(a)))
    ellipse(screen, color,
            (x + 150 * a - (np.abs(a) - a) * 30 / 2, y + 605 * np.abs(a), 30 * np.abs(a), 70 * np.abs(a)))
    ellipse(screen, color,
            (x + 141 * a - (np.abs(a) - a) * 27 / 2, y + 668 * np.abs(a), 27 * np.abs(a), 15 * np.abs(a)))
    polygon(screen, (0, 0, 0),
            [(x + 160 * a, y + 620 * np.abs(a)), (x + 230 * a, y + 620 * np.abs(a)), (x + 230 * a, y + 550 * np.abs(a)),
             (x + 160 * a, y + 550 * np.abs(a))])
    polygon(screen, color,
            [(x + 162 * a, y + 618 * np.abs(a)), (x + 228 * a, y + 618 * np.abs(a)), (x + 228 * a, y + 552 * np.abs(a)),
             (x + 162 * a, y + 552 * np.abs(a))])
    ellipse(screen, (0, 0, 0),
            (x + 151 * a - (np.abs(a) - a) * 20 / 2, y + 548 * np.abs(a), 20 * np.abs(a), 30 * np.abs(a)))
    ellipse(screen, color,
            (x + 153 * a - (np.abs(a) - a) * 16 / 2, y + 550 * np.abs(a), 16 * np.abs(a), 26 * np.abs(a)))
    ellipse(screen, (0, 0, 0),
            (x + 221 * a - (np.abs(a) - a) * 20 / 2, y + 548 * np.abs(a), 20 * np.abs(a), 30 * np.abs(a)))
    ellipse(screen, color,
            (x + 223 * a - (np.abs(a) - a) * 16 / 2, y + 550 * np.abs(a), 16 * np.abs(a), 26 * np.abs(a)))
    ellipse(screen, (255, 255, 255),
            (x + 175 * a - (np.abs(a) - a) * 15 / 2, y + 572 * np.abs(a), 15 * np.abs(a), 5 * np.abs(a)))
    ellipse(screen, (255, 255, 255),
            (x + 200 * a - (np.abs(a) - a) * 15 / 2, y + 572 * np.abs(a), 15 * np.abs(a), 5 * np.abs(a)))
    ellipse(screen, (0, 0, 0),
            (x + 205 * a - (np.abs(a) - a) * 6 / 2, y + 572 * np.abs(a), 6 * np.abs(a), 6 * np.abs(a)))
    ellipse(screen, (0, 0, 0),
            (x + 180 * a - (np.abs(a) - a) * 6 / 2, y + 572 * np.abs(a), 6 * np.abs(a), 6 * np.abs(a)))
    polygon(screen, (255, 255, 255), [(x + 180 * a, y + 602 * np.abs(a)), (x + 183 * a, y + 592 * np.abs(a)),
                                      (x + 185 * a, y + 598 * np.abs(a))])
    polygon(screen, (255, 255, 255), [(x + 207 * a, y + 602 * np.abs(a)), (x + 202 * a, y + 598 * np.abs(a)),
                                      (x + 204 * a, y + 592 * np.abs(a))])
    arc(screen, (0, 0, 0),
        (x + 175 * a - (np.abs(a) - a) * 40 / 2, y + 600 * np.abs(a), 40 * np.abs(a), 20 * np.abs(a)), 0, np.pi)


def dog_house(x, y):
    """
    функция рисует будку всесте с цепь
    :param x: параметр, отвечающий за положение будки пр координате x
    :param y: параметр, отвечающий за положение будки пр координате y
    """
    polygon(screen, (0, 0, 0), [(x + 380, 555), (x + 380, y + 455), (x + 440, y + 395), (x + 480, y + 375), (x + 520, y + 455), (x + 520, y + 535), (x + 485, y + 615)])
    polygon(screen, (200, 200, 0), [(x + 381, y + 554), (x + 381, y + 454), (x + 484, y + 494), (x + 484, y + 613)])
    polygon(screen, (220, 220, 0), [(x + 383, y + 453), (x + 441, y + 394), (x + 484, y + 492)])
    polygon(screen, (220, 220, 0), [(x + 480, y + 376), (x + 443, y + 394), (x + 486, y + 492), (x + 518, y + 454)])
    polygon(screen, (200, 200, 0), [(x + 486, y + 495), (x + 519, y + 457), (x + 519, y + 533), (x + 485, y + 613)])
    ellipse(screen, (0, 0, 0), (x + 402, y + 500, 55, 60))
    ellipse(screen, (0, 0, 0), (x + 395, y + 550, 20, 10), 1)
    ellipse(screen, (0, 0, 0), (x + 377, y + 570, 25, 20), 1)
    ellipse(screen, (0, 0, 0), (x + 387, y + 553, 20, 25), 1)
    ellipse(screen, (110, 110, 110), (x + 388, y + 554, 18, 23))
    ellipse(screen, (0, 0, 0), (x + 367, y + 587, 25, 10), 1)
    ellipse(screen, (0, 0, 0), (x + 362, y + 592, 13, 13), 1)
    ellipse(screen, (0, 0, 0), (x + 340, y + 597, 30, 10), 1)
    ellipse(screen, (0, 0, 0), (x + 328, y + 600, 20, 10), 1)
    ellipse(screen, (0, 0, 0), (x + 308, y + 600, 30, 5), 1)
    ellipse(screen, (0, 0, 0), (x + 301, y + 597, 12, 15), 1)
    ellipse(screen, (0, 0, 0), (x + 290, y + 605, 18, 8), 1)
    ellipse(screen, (0, 0, 0), (x + 280, y + 611, 17, 10), 1)


polygon(screen, (0, 150, 200), [(0, 0), (600, 0), (600, 400), (0, 400)])
polygon(screen, (70, 230, 150), [(0, 401), (600, 401), (600, 800), (0, 800)])

fence(100, 20, 500, 380, 13, (180, 0, 0))
fence(-10, 200, 350, 250, 14, (0, 170, 0))
fence(300, 300, 350, 200, 13, (160, 160, 0))
fence(-5, 350, 250, 200, 13, (120, 120, 0))
dog(-150, -200, 1.2, (110, 110, 110))
dog(420, 80, -1, (0, 150, 150))
dog(680, 200, -0.5, (70, 70, 0))
dog_house(-60, 0)
dog(10, -780, 2.5, (80, 0, 80))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
