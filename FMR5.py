from functools import reduce

CheckEven = lambda No:((No%2) == 0)

Multiby2 = lambda No : No*2

Summation = lambda No1,No2 : No1+No2 
    


def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    
    print("Data is :",Data_Input)
    
    Data_Filter = list(filter(CheckEven,Data_Input))
    print("Filter Data : ",Data_Filter)

    Data_Map = list(map(Multiby2, Data_Filter))
    print("Mapped Data :",Data_Map)

    Data_Reduce = reduce(Summation,Data_Map)
    print("Reuced Data :",Data_Reduce)




if __name__ == "__main__":
    main()
