print("Assignment:1 ,Quesion :2")

def Addition(value1, value2):
    Ans = value1 + value2
    return Ans

def main():
    print("Enter First Number:")
    No1 = int(input())
    print("Enter Second Number:")
    No2 = int(input())

    Ret = Addition(No1 ,No2)

    print("Addition is :",Ret)


if __name__ == "__main__":
    main()