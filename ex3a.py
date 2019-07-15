##this program is for the exercise 3a
def main():
    startamount= input("please gimme a start amount of money in dollars.cents: ")
    targetamount= input("please gimme a target amount of money in dollars.cents: ")
    annualinterest= input("please gimme an interest rate: ")
    startamount= float(startamount)
    targetamount= float(targetamount)
    annualinterest=float(annualinterest)
    i=0
    newtargetamount=0
    while newtargetamount<=targetamount:
        newtargetamount=startamount*(1+annualinterest)
        startamount=newtargetamount
        i=i+1
        ##why I cannot use return i here
        ##what does that exactly mean of returni
        ##return to i=0?
    print(i, " years")
if __name__ == '__main__':
    main()
