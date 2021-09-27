import turtle

turtle.shape('circle')
Vx = 10
Vy = 40
x = 0
y = 0
while Vy >= 1:
    while y >= 0:
        turtle.goto(x, y)
        x = x + Vx*0.01
        y = y + Vy*0.01
        Vy = Vy - 0.098
    Vy = Vy*(-0.7)
    y = (-1)*y