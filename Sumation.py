print("Welcome ")

def main():
   
    print("Enter Number limit")
    num = int(input())

    print("List of Number :")
    for i in range(1,num):
        print(i)
    
    Ret = sum(range(1,num))
    print("Sumation of Number :",Ret)

if __name__ == "__main__":
    main()
    