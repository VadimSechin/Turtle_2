import turtle

turtle.shape('turtle')

input = open('commands.txt', 'r')
A = input.readline()
A = A.rstrip()
N0 = input.readline()
N0 = N0.rstrip()
N1 = input.readline()
N1 = N1.rstrip()
N2 = input.readline()
N2 = N2.rstrip()
N3 = input.readline()
N3 = N3.rstrip()
N4 = input.readline()
N4 = N4.rstrip()
N5 = input.readline()
N5 = N5.rstrip()
N6 = input.readline()
N6 = N6.rstrip()
N7 = input.readline()
N7 = N7.rstrip()
N8 = input.readline()
N8 = N8.rstrip()
N9 = input.readline()
N9 = N9.rstrip()

B0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(N0), 1):
    if N0[i] == 'a':
        B0[i] = 40 * 2 ** 0.5
    else:
        B0[i] = int(N0[i])

for i in range(0, len(N1), 1):
    if N1[i] == 'a':
        B1[i] = 40 * 2 ** 0.5
    else:
        B1[i] = int(N1[i])

for i in range(0, len(N2), 1):
    if N2[i] == 'a':
        B2[i] = 40 * 2 ** 0.5
    else:
        B2[i] = int(N2[i])

for i in range(0, len(N3), 1):
    if N3[i] == 'a':
        B3[i] = 40 * 2 ** 0.5
    else:
        B3[i] = int(N3[i])

for i in range(0, len(N4), 1):
    if N4[i] == 'a':
        B4[i] = 40 * 2 ** 0.5
    else:
        B4[i] = int(N4[i])

for i in range(0, len(N5), 1):
    if N5[i] == 'a':
        B5[i] = 40 * 2 ** 0.5
    else:
        B5[i] = int(N5[i])

for i in range(0, len(N6), 1):
    if N6[i] == 'a':
        B6[i] = 40 * 2 ** 0.5
    else:
        B6[i] = int(N6[i])

for i in range(0, len(N7), 1):
    if N7[i] == 'a':
        B7[i] = 40 * 2 ** 0.5
    else:
        B7[i] = int(N7[i])

for i in range(0, len(N8), 1):
    if N8[i] == 'a':
        B8[i] = 40 * 2 ** 0.5
    else:
        B8[i] = int(N8[i])

for i in range(0, len(N9), 1):
    if N9[i] == 'a':
        B9[i] = 40 * 2 ** 0.5
    else:
        B9[i] = int(N9[i])
C = [0, 0, 0, 0, 0, 0]
for i in range(0, len(A), 1):
    C[i] = int(A[i])

Q = [B0, B1, B2, B3, B4, B5, B6, B7, B8, B9]

for j in range(0, len(C), 1):
    for i in range(9):
        if Q[C[j]][0 + 6 * i] == 1:
            turtle.pendown()
        if Q[C[j]][0 + 6 * i] == 0:
            turtle.penup()
        turtle.forward(Q[C[j]][1 + 6 * i] * 10 + Q[C[j]][2 + 6 * i])
        turtle.left(Q[C[j]][3 + 6 * i] * 100 + Q[C[j]][4 + 6 * i] * 10 + Q[C[j]][5 + 6 * i])
    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)