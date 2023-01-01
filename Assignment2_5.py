
def Prime(Num):
    flag = False
    if Num > 1:
        for i in range(2,Num,1):
            if(Num % i)== 0:
                flag = True
                break

    if flag :
        print("It is not Prime Number")
    else:
        print("It is Prime Number")

def main():
    print("Enter the Number ")
    Num = int(input())

    Prime(Num)

if __name__ == "__main__":
    main()