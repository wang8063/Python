# baby it is cold outside
import math
def main():
    t=input("Enter temperature (F): ")
    t=float(t)
    v=input("Enter wind velocity (MPH): ")
    v=float(v)
    twc= 35.74 + 0.6215* t - 35.75* pow(v,0.16)+ 0.4275* t* pow(v,0.16)
    print("The windchill is: " , twc)
if __name__ == '__main__':
    main() 
