from turtle import *

speed(120)

def drawFractalLine(length, depth):
    if depth == 0:
        forward(length)
    else:
        drawFractalLine(length/3, depth-1)
        right(60)
        drawFractalLine(length/3, depth-1)
        left(120)
        drawFractalLine(length/3, depth-1)
        right(60)
        drawFractalLine(length, depth-1)
for i in range(6):
    drawFractalLine(200, 4)
    right(60)

main()
