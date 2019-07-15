import random
def main():
    a=random.randint(1,6)
    b=random.randint(1,6)
    print('Initial roll is: ','[',a,',',b,']','=',a+b)
    if a+b==7 or a+b==11:
        print('You win!')
    else:
        print('Roll is: ',a+b,'Roll again')
        x=random.randint(1,6)
        y=random.randint(1,6)
        while (x+y)!=7:
            x=random.randint(1,6)
            y=random.randint(1,6)
        print('Roll is: ',x+y,'Sorry, you lose')
        while x+y==a+b:
            print('Roll is: ','[',a,',',b,']','=',a+b,'You win!')


if __name__ == '__main__':
    main()
