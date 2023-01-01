from functools import reduce

def main():
    print("Enter size of element:")
    iSize = int(input())

    Data =[]
    print("Enter the element of Data:")
    for No in range(0,iSize,1):
        Values = int(input())
        Data.append(Values)

    print("Values of Data :",Data)

    Data_filter=list(filter(lambda No: 70 <= No <= 90 ,Data))
    print("Filtered Data :",Data_filter)

    Data_map =list(map(lambda No: No+10,Data_filter))
    print("Mapped Data :",Data_map)

    Data_reduce = reduce(lambda No1,No2 : No1*No2,Data_map)
    print("Reduced Data :",Data_reduce)

   

if __name__=="__main__":
    main()