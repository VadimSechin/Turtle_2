from random import randint
import turtle

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
for i in range(4):
    turtle.forward(400)
    turtle.right(90)
turtle.penup()
number_of_turtles = 7
steps_of_time_number = 100

V = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(14):
    V[i] = randint(-30, 30)

X = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(14):
    X[i] = randint(-200, 200)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for i in range(number_of_turtles):
    unit = pool[i]
    unit.penup()
    unit.speed(50)
    unit.goto(X[i], X[i + 7])

for j in range(steps_of_time_number):
    for i in range(number_of_turtles):
        unit = pool[i]
        unit.goto(X[i] + V[i] / 5, X[i + 7] + V[i + 7] / 5)
        X[i] = X[i] + V[i] / 5
        X[i + 7] = X[i + 7] + V[i + 7] / 5
        if X[i] >= 200 or X[i] <= -200:
            V[i] = (-1) * V[i]
        if X[i + 7] >= 200 or X[i + 7] <= -200:
            V[i + 7] = (-1) * V[i + 7]