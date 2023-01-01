def main():
    print("Enter number to printing ")
    num = int(input())
    k = 1
    for i in range(1,num+1):
        for j in range(0,k):
            print(i, end=" \t")
        k = k + 1
        
        print()


if __name__=="__main__":
    main()