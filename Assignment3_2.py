def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)
    
    maximum = 0
    for iCnt in range(0,iSize,1):
        maximum =max(maximum,Data_Input[iCnt])

    print("Maximum of array :",maximum)


if __name__ == "__main__":
    main()