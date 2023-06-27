import turtle
import random

tSize = 10
r, g, b = 0.0, 0.0, 0.0

def setOnClickListenerLeft(x,y):
    global r, g, b
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.shapesize(tSize)
    turtle.pensize(tSize)
    turtle.goto(x,y)
    turtle.circle(tSize)

    for i3 in range(0, 5):
        turtle.forward(150)
        turtle.left(144)

    turtle.left(72)
    turtle.forward(92)

    for i4 in range(0, 4):
        turtle.right(72)
        turtle.forward(92)
               
# def  setOnClickListenerMid(x,y):

turtle.title('거북이 테스트')
turtle.shape('turtle')
turtle.pensize(tSize)

turtle.onscreenclick(setOnClickListenerLeft, 1)

turtle.done()