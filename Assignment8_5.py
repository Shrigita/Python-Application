def Fact(No):
    if(No <=0):
        return 1
    else:
        return (No * Fact(No-1))

def main():
    print("Enter Number for factorial :")
    No =int(input())

    Ret = Fact(No)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()