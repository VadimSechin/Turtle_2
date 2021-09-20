import turtle


def duga(a, r):
    for i in range(a):
        turtle.forward(r)
        turtle.right(1)


turtle.shape('turtle')
turtle.left(180)
turtle.penup()
turtle.forward(200)
turtle.right(90)
turtle.pendown()
for s in range(4):
    duga(180, 1.3)
    duga(180, 0.25)