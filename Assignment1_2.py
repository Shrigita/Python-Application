print("Assignment:1 ,Quesion :2")

def ChkNum(No):
    if No%2 == 0:
        return 1
    else:
        return 0

def main():
    print("Enter Number Please :")
    Num = int(input())

    Ret = ChkNum(Num)

    if Ret == 1:
        print("Even Number")
    else :
        print("Odd Number")


if __name__ == "__main__":
    main()