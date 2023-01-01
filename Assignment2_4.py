
def DisplayFactors(No):
    sum = 0
    print("Factors are :")
    for i in range(1,No):
        if ((No % i) == 0):
            print(i,end=",")
            sum = sum + i

    print()
    print("Sum of factors "+str(No)+" is = "+str(sum))
   

def main():
    print("Enter the Number :")
    Num = int(input())

    DisplayFactors(Num)

if __name__ == "__main__":
    main()