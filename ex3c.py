import turtle
import math
turtle.showturtle()
def main():
    turtle.home()
    turtle.dot(40,'yellow')
    turtle.penup()
    angle=0
    length=150
    turtle.shape('circle')
    turtle.shapesize(1)
    ##degree?
    while angle< 3*6.28319:
        x= length* math.cos(angle)
        y= length* math.sin(angle)
        turtle.goto(x,y)
        angle=angle+0.017
    turtle.end_fill()
if __name__ == '__main__':
    main()
