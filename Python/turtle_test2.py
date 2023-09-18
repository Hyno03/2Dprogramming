import turtle

def draw_circle(x,y,r):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x,y+r)
    turtle.stamp()
    
draw_circle(0,0,50)
draw_circle(200,200,100)
draw_circle(100,-100,50) 
