import math
##perfect(n) what is the n means. How to use argument
def perfect(n):
    s=0
    for i in range (1,n,1):
        if n % i==0:
            s=s+i
    if s==n:
        return True
    else:
        return False

def main():
    x=input("enter lower bound: ")
    y=input("enter upper bound: ")
    x=int(x)
    y=int(y)
    for n in range (x, y+1, 1):
        perfect(n)
        if perfect(n):
            print(n)
        ##how to connect two functions here
        ##how to print the bool==true


if __name__ == '__main__':
    main()
