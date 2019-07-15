# calculate the number of bars that a person need
import math
def main():
    w=input("please gimee your weight: ")
    w=float(w)
    h=input("and ur height: ")
    h=float(h)
    a=input("age, please: ")
    a=float(a)
    sex=input("your gender:(M) or (F) ")
    if sex== "M":
        bmr= 66+ (6.3* w)+ (12.9* h)- (6.8* a)
    else:
        bmr= 655 + (4.3* w)+ (4.7* h)- (4.7* a)
    n= bmr/230
    print("your bmr is" , bmr)
    print("the # of chocolates u need", n)

if __name__ == '__main__':
    main()
