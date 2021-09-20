import turtle
import numpy as np

def star(x, y, r, n):
    turtle.goto(x + r*np.cos(np.pi*2/n), y + r*np.sin(np.pi*2/n))
    turtle.pendown()
    for i in range(int((n - 1)/2)):
        turtle.goto(x + r*np.cos(np.pi*2*((n + 1)/2 - i)/n), y + r*np.sin(np.pi*2*((n + 1)/2 - i)/n))
        turtle.goto(x + r*np.cos(np.pi*2*(n - i)/n), y + r*np.sin(np.pi*2*(n - i)/n))
    turtle.goto(x + r*np.cos(np.pi*2/n), y + r*np.sin(np.pi*2/n))

turtle.shape('turtle')
turtle.penup()
star(-50, -50, 100, 5)
turtle.penup()
star(150, 150, 100, 11)