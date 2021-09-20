import turtle

turtle.shape('turtle')
turtle.penup()
turtle.goto(30, 0)
turtle.left(90)
turtle.pendown()
for i in range(360):
    turtle.forward(2)
    turtle.left(1) 