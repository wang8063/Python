#this program wants to draw a star by using turtle
import turtle
turtle.showturtle()

def main():
    sidelength= turtle.numinput("Welcome to turtle world!","please enter the length you want")
    turtle.left(36)
    turtle.fd(sidelength)
    for i in range(0,4):
        turtle.left(144)
        turtle.fd(sidelength)
if __name__ == '__main__':
    main()
