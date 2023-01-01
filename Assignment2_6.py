def main():
    print("Enter number to printing *")
    num = int(input())
    k = num
    for i in range(0,num):
        for j in range (0, k):
            print("*", end=" \t")
        k= k-1
        print()


if __name__=="__main__":
    main()