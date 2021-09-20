import turtle

turtle.shape('turtle')
n = 12
for i in range(1, n + 1, 1):
    turtle.forward(140)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(140)
    turtle.right(180 + 360/n)