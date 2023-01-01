def main():
    print("Enter number to printing *")
    num = int(input())
    for i in range(1,num+1,1):
        for i in range (1,num+1,1):
            print("*", end=" \t")
        print()


if __name__=="__main__":
    main()