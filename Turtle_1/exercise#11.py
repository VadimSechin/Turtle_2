import turtle
import numpy as np


def mnogo(r, n):
    for i in range(360):
        turtle.forward(r / 10)
        turtle.left(1)
    for i in range(360):
        turtle.forward(r / 10)
        turtle.right(1)


turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
for n in range(5):
    mnogo(5 + 2 * n, 50)