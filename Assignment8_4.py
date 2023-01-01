list1 = []
def SumDigit(No):
    if(No == 0):
        return list1
    digit =No%10
    list1.append(digit)
    SumDigit(No//10)

    return sum(list1)
    

def main():
    print("Enter Number for Summation of Digit :")
    No =int(input())

    Ret = SumDigit(No)
    print("Summation of digit is : ",Ret)

if __name__ == "__main__":
    main()