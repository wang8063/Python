import random
import turtle
import math
def matrix(n,init):
    a=[0]*n
    for i in range(len(a)):
        a[i]= [init] *n
    return a
def populate(m,radius):
    #print('a')
    newm=[x[:] for x in m]
    #print(newm)
    times=0
    while times<1000:
        i=random.randint(-50,50)
        j=random.randint(-50,50)
        if i**2+j**2<=radius**2:
            #print(i,j)
            if newm[i][j]!=1:
                newm[i][j]=1
                times=times+1
    return newm

def showMatrix(turtle_object,m):
    #print('b')
    for i in range(len(m)):
        for j in range(len(m)):
            if (m[i][j]==1):
                turtle_object.goto(i,j)
                turtle_object.shape("square")
                turtle_object.shapesize(0.2)
                turtle_object.stamp()
def neighbors(m,row,col,radius):
    count=0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            count=count+m[i][j]
    return count

def update(newm,radius):
    new_grid=[x[:] for x in newm]
    for i in range(-50,51):
        for j in range(-50,51):
            count=neighbors(newm,i,j,radius)
            #print('count is: ',count)
            if i**2+j**2<=radius**2:
                if newm[i][j]==1:
                    count=count-1
                    if count<2:
                        new_grid[i][j]=0
                    elif count>3:
                        new_grid[i][j]=0
                    elif count==2 or count==3:
                        new_grid[i][j]=1
                elif newm[i][j]==0:
                    if count==3:
                        new_grid[i][j]=1
    return new_grid


def main():
    i=0
    turtle_object=turtle.Turtle()
    screen= turtle_object.getscreen()
    screen.setworldcoordinates(-50,-50,50,50)
    radius=screen.numinput('Please gimme a radius!','radius')
    turtle_object.penup()
    #turtle_object.hideturtle()
    m=matrix(100,0)
    new_grid=populate(m,radius)
    screen.tracer(0)
    while i <=50:
        #print("new m is",newm)
        showMatrix(turtle_object, new_grid)
        #screen.delay(2000)
        screen.update()
        #user=input("enter whatever")
        new_grid=update(new_grid,radius)
#showMatrix(turtle_object,new_grid)
        turtle_object.clear()
        i=i+1

if __name__ == '__main__':
    main()
