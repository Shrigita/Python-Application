print("Assignment:1 ,Quesion :6")

def main():
    print("Enter Number to check + or - :")
    No = int(input())

    if No > 0 :
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else :
        print("Zero")

if __name__ == "__main__":
    main()