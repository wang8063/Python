import turtle
import math
turtle.hideturtle()
def main():
    turtle.dot(50,"yellow")
    moonturtle= turtle.Turtle()
    moonturtle.shape("circle")
    moonturtle.shapesize(0.5)
    moonturtle.color('green')
    moonturtle.penup()
    planetturtle= turtle.Turtle()
    planetturtle.shape("circle")
    planetturtle.shapesize(1)
    planetturtle.color('blue')
    planetturtle.home()
    planetturtle.penup()
    angle1=0
    angle2=0
    lengthp=150
    lengthm=80
    ##degree?
    while angle1< 6.28319:
        px= lengthp* math.cos(angle1)
        py= lengthp* math.sin(angle1)
        planetturtle.goto(px,py)
        angle1=angle1+2*0.017
        angle2=0
        while angle2< 6.28319:
            mx=px+ lengthm* math.cos(angle2)
            my=py+ lengthm* math.sin(angle2)
            moonturtle.goto(mx,my)
            angle2=angle2+5*0.017

if __name__ == '__main__':
    main()
