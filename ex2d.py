#this program can connect two points and build its slope-intercept equation
import math
def main():
    x1= input("Enter first x value: ")
    y1= input("Enter first y value: ")
    x2= input("Enter second x value: ")
    y2= input("Enter second y value: ")
    x1=float(x1)
    x2=float(x2)
    y1=float(y1)
    y2=float(y2)


    if x2==x1:
        b=y1
        print("y=",b)
    else:
        m= (y2-y1)/(x2-x1)
        b=y1-m*x1
        print("y=",m,"x+",b)
if __name__ == '__main__':
    main()
