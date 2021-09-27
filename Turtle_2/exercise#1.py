from random import *
import turtle

turtle.shape('turtle')
for i in range(200):
    turtle.forward(randint(10, 100))
    turtle.left(randint(1, 360))