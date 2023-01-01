class Demo: 
     def __init__(self,A,B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

     def Fun(self):
        print("Value of No1 variable in Fun",self.No1)
        print("Value of No2 variable in Fun",self.No2)

     def Gun(self):
        print("Value of No1 variable in Gun",self.No1)
        print("Value of No2 variable in Gun",self.No2)


def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()