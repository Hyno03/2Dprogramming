import turtle
import random

def drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,300))
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(drunken_move, ' ')
turtle.onkey(restart, ' Escape')
turtle.listen()
