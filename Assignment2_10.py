def getSum(No):
    sum = 0
    for digit in str(No):
        sum += int(digit)
    return sum 

def main():
    print("Enter the Number:")
    Num = int(input())

    Ret = getSum(Num)

    print("sum of digit =",Ret)
    
if __name__ == "__main__":
    main()