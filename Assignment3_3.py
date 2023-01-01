def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)
    
   
    for iCnt in range(1,iSize,1):
        minimum =Data_Input[0]
        minimum = min(minimum,Data_Input[iCnt])

    print("Minimum of array :",minimum)


if __name__ == "__main__":
    main()