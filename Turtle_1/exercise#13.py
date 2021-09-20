import turtle


def circle(x, y, r):
    turtle.goto(x - r, y + 1)
    turtle.goto(x - r, y)
    turtle.pendown()
    turtle.width(1)
    turtle.color('black')
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(r / 100)
        turtle.right(1)


def duga(x, y, r):
    turtle.goto(x + r, y + 1)
    turtle.goto(x + r, y)
    turtle.pendown()
    turtle.right(90)
    for i in range(180):
        turtle.forward(r / 50)
        turtle.right(1)


turtle.shape('turtle')
turtle.penup()
circle(200, 100, 200)
turtle.color('yellow')
turtle.end_fill()
turtle.penup()
circle(-20, 30, 20)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
circle(50, 30, 20)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.width(10)
turtle.color('brown')
turtle.goto(0, -40)
turtle.penup()
turtle.color('red')
duga(5, -50, 40)