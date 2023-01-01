
class Arithematic:
    def __init__(self):
        print("Inside init method")
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter First Number :")
        self.Value1 = int(input())
        print("Enter Second Number :")
        self.Value2 = int(input())

    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans

    def Substraction(self):
        Ans = self.Value1 - self.Value2
        return Ans


    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans


    def Division(self):
        Ans = self.Value1 / self.Value2
        return Ans


def main():
    print("Inside main method")

    obj = Arithematic()

    obj.Accept()

    Ret =obj.Addition()
    print("Addition is ",Ret)

    Ret =obj.Substraction()
    print("Substraction is ",Ret)

    Ret =obj.Multiplication()
    print("Multiplication is ",Ret)

    Ret =obj.Division()
    print("Division is ",Ret)

if __name__ =="__main__":
    print("Inside starter")
    main()