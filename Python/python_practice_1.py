import turtle
shape = input("Enter Shape:")
if shape == 'circle':
    turtle.reset()
    turtle.circle(50)
elif shape == 'triangle':
    turtle.reset()
    turtle.forward(50); turtle.left(120)
    turtle.forward(50); turtle.left(120)
    turtle.forward(50)
else:
    print('Unknown shape')
