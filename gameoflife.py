import random
import turtle
import numpy as np
def matrix(n,init):
    a=[0]*n
    for i in range(len(a)):
        a[i]= [init] *n
    return a
def populate(m,radius):
    #print('a')
    newm=np.pad(m,1,mode='wrap')
    #print(newm)
    times=0
    while times<500:
        i=random.randint(len(m)/2-radius,radius+len(m)/2)
        j=random.randint(len(m)/2-radius,radius+len(m)/2)
        if pow(i-len(m)/2,2)+pow(j-len(m)/2,2)<=pow(radius,2):
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
def neighbors(m,row,col):
    count=0

    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            count=count+m[i][j]
                    #print("count is: ",count)
    return count

def update(newm):
    new_grid=[x[:] for x in newm]
    for i in range(0,100):
        for j in range(0,100):
            count=neighbors(newm,i,j)
            #print('count is: ',count)
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
    screen.setworldcoordinates(0,0,100,100)
    radius=screen.numinput('Please gimme a radius!','radius')
    turtle_object.penup()
    #turtle_object.hideturtle()
    m=matrix(100,0)
    m=np.pad(m,1,mode='wrap')
    new_grid=populate(m,radius)
    screen.tracer(0)
    while i <=50:
        #print("new m is",newm)
        showMatrix(turtle_object, new_grid)
        #screen.delay(2000)
        screen.update()
        #user=input("enter whatever")
        new_grid=update(new_grid)
#showMatrix(turtle_object,new_grid)
        turtle_object.clear()
        i=i+1

if __name__ == '__main__':
    main()
