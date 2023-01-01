import MarvellousNum

def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)
    Result = []
    for iCnt in range(0,iSize,1):
        
        if (MarvellousNum.ChkPrime(Data_Input[iCnt])) == True:
            Result.append(Data_Input[iCnt])

    print("Prime data :",Result)

    

if __name__ == "__main__":
    main()