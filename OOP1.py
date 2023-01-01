
class Arithematic:
    def __init__(self,A,B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans


def main():
    print("Inside main method")

    obj = Arithematic(11,10)

    Ret =obj.Addition()
    print("Addition is ",Ret)

    Ret =obj.Substraction()
    print("Substraction is ",Ret)

    objX = Arithematic(21,20)

    Ret =objX.Addition()
    print("Addition is ",Ret)

    Ret =objX.Substraction()
    print("Substraction is ",Ret)
    

if __name__ =="__main__":
    print("Inside starter")
    main()