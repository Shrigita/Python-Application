print("Assignment:1 ,Quesion :7")

def ChkNum(No):
    if No%5 == 0:
        return 1
    else:
        return 0

def main():
    print("Enter Number to check number is divisible by 5 or not :")
    Num = int(input())

    Ret = ChkNum(Num)

    if Ret == 1:
        print("True")
    else :
        print("False")


if __name__ == "__main__":
    main()