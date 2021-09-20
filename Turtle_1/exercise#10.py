import turtle


def krug(r, n):
    for i in range(720):
        turtle.forward(0.5)
        turtle.left(0.5)
    for i in range(720):
        turtle.forward(0.5)
        turtle.right(0.5)


turtle.shape('turtle')
turtle.speed(10)
for n in range(3):
    krug(50, 50)
    turtle.left(60) 