import turtle

turtle.shape('turtle')
for i in range(10):
    turtle.penup()
    turtle.goto(0 - 10*i, 0 - 10*i)
    turtle.pendown()
    for j in range(4):
        turtle.forward(40 + 20*i)
        turtle.left(90) 