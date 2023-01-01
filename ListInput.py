def main():
    Arr = list()

    print("Enter How Many Element you want to store?")
    size = int(input())
    
    print("Please Enter the values")
    for i in range(0,size):
        no = int(input())
        #Arr.append(no)
        Arr.insert(i,no)

    print(Arr)

    




if __name__ == "__main__":
    main()