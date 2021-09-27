import turtle

N0 = (1, 40, 90, 1, 40, 0, 1, 40, 90, 1, 40, 90, 1, 40, 0, 1, 40, 135, 0, 40*2**0.5, 135, 0, 40, 225, 0, 40*2**0.5, 315)
N1 = (0, 40, 90, 1, 40, 0, 1, 40, 90, 0, 40, 90, 0, 40, 0, 0, 40, 135, 0, 40*2**0.5, 135, 0, 40, 225, 1, 40*2**0.5, 315)
N2 = (1, 40, 90, 0, 40, 0, 1, 40, 90, 1, 40, 90, 0, 40, 0, 0, 40, 135, 1, 40*2**0.5, 135, 0, 40, 225, 0, 40*2**0.5, 315)
N3 = (0, 40, 90, 0, 40, 0, 0, 40, 90, 1, 40, 90, 0, 40, 0, 0, 40, 135, 1, 40*2**0.5, 135, 1, 40, 225, 1, 40*2**0.5, 315)
N4 = (0, 40, 90, 1, 40, 0, 1, 40, 90, 0, 40, 90, 1, 40, 0, 0, 40, 135, 0, 40*2**0.5, 135, 1, 40, 225, 0, 40*2**0.5, 315)
N5 = (1, 40, 90, 1, 40, 0, 0, 40, 90, 1, 40, 90, 1, 40, 0, 0, 40, 135, 0, 40*2**0.5, 135, 1, 40, 225, 0, 40*2**0.5, 315)
N6 = (1, 40, 90, 1, 40, 0, 0, 40, 90, 0, 40, 90, 0, 40, 0, 1, 40, 135, 0, 40*2**0.5, 135, 1, 40, 225, 1, 40*2**0.5, 315)
N7 = (0, 40, 90, 0, 40, 0, 0, 40, 90, 1, 40, 90, 0, 40, 0, 1, 40, 135, 0, 40*2**0.5, 135, 0, 40, 225, 1, 40*2**0.5, 315)
N8 = (1, 40, 90, 1, 40, 0, 1, 40, 90, 1, 40, 90, 1, 40, 0, 1, 40, 135, 0, 40*2**0.5, 135, 1, 40, 225, 0, 40*2**0.5, 315)
N9 = (0, 40, 90, 0, 40, 0, 1, 40, 90, 1, 40, 90, 1, 40, 0, 0, 40, 135, 1, 40*2**0.5, 135, 1, 40, 225, 0, 40*2**0.5, 315)
A=[N0, N1, N2, N3, N4, N5, N6, N7, N8, N9]

turtle.shape('turtle')
for j in 1, 4, 1, 7, 0, 0:
    for i in range(9):
        if A[j][0 + 3*i]==1:
            turtle.pendown()
        if A[j][0 + 3*i]==0:
            turtle.penup()
        turtle.forward(A[j][1 + 3*i])
        turtle.left(A[j][2 + 3*i])
    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)