import turtle
import numpy as np


def mnogo(r, n):
    turtle.left(90 + 180 / n)
    a = 2 * r * np.sin(np.pi / n)
    turtle.pendown()
    for i in range(1, n + 1, 1):
        turtle.forward(a)
        turtle.left(360 / n)


turtle.penup()
turtle.shape('turtle')
turtle.forward(200)
for n in range(3, 12, 1):
    mnogo(30 + 25 * n, n)
    turtle.penup()
    turtle.right(90 + 180 / n)
    turtle.forward(10) 