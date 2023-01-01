#Position/Keyword arguments
def Add1(No1,No2):
    print("Value of No1 :",No1)
    print("Value of No2 :",No2)
    return No1 + No2

def sub1(No1,No2):
    print("Value of No1 :",No1)
    print("Value of No2 :",No2)
    return No1 - No2


def main():
    Ans = Add1(10,20)        #Positional Argument
    print("Addition =",Ans)

    Ans = sub1(No2 = 10, No1 = 11)    #Keyword Argument
    print("Subtraction =",Ans)

    Ans = sub1(No1 = 10,No2 = 11)
    print("Subtraction =",Ans)

if __name__ == "__main__":
    main()