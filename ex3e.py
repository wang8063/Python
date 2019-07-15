import math
def gcd(a,b):
    if a>b:
        r=a%b
        if r != 0:
            a=b
            b=r
            while a%b!=0:
                r=a%b
                a=b
                b=r
    else:
        b=a
    return(b)
def main():
    a=abs(int(input("enter first value: ")))
    while a!="":
        b=abs(int(input("enter second value: ")))
        g=gcd(a,b)
        print('the GCD of',a,'and',b,'is',g)
        a=input("enter first value: ")
        if a !="":
            a=abs(int(a))
        elif a=="":
            print('enter first value: ')

if __name__ == '__main__':
    main()
