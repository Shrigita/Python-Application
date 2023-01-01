from functools import reduce

def main():
    print("Enter number of element in list :")
    iSize = int(input())

    Data_Input = []
    print("Plz Enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    
    print("Data is :",Data_Input)
    
    Data_Filter = list(filter( lambda No:(No%2) == 0, Data_Input))
    print("Filter Data : ",Data_Filter)

    Data_Map = list(map( lambda No : No*2, Data_Filter))
    print("Mapped Data :",Data_Map)

    Data_Reduce = reduce(lambda No1,No2 : No1+No2 ,Data_Map)
    print("Reuced Data :",Data_Reduce)




if __name__ == "__main__":
    main()
