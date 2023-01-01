def CheckEven(No):
    return ((No%2) == 0)
     
def filterX(Helper_Function,Data):
    Result = []
    for No in Data:
        if(Helper_Function(No)== True):
            Result.append(No)
    return Result

def Multiby2(No):
    return No*2

def mapX(Helper_Function1,Data1):
    Result =[]
    for No in Data1:
            Value = Helper_Function1(No)
            Result.append(Value)
    return Result

def Summation(No1,No2):
    return No1+No2 

def reduceX(Helper_Function,Data):
    Ans = 0
    for No in Data:
        Ans =Helper_Function(Ans,No)
        
    return Ans

def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    
    print("Data is :",Data_Input)
    
    Data_Filter = filterX(CheckEven,Data_Input)
    print("Filter Data : ",Data_Filter)

    Data_Map = mapX(Multiby2, Data_Filter)
    print("Mapped Data :",Data_Map)

    Data_Reduce = reduceX(Summation,Data_Map)
    print("Reuced Data :",Data_Reduce)




if __name__ == "__main__":
    main()
