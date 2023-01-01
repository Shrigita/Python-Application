def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)
    
    print("Enter number to check frequency in list :")
    freq = int(input())
    count = 0
    for iCnt in range(0,iSize,1):
        if freq == Data_Input[iCnt]:
            count += 1
        else :
             count += 0
    print("Frequency is :",count)

if __name__ == "__main__":
    main()