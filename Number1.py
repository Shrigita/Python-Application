class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()  #[]
   
    def Accept(self):
         print("How many element you want to store?")
         self.Size =int(input())

         print("Please enter the elements")
         for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elemnts from list are :")
        for i in range(0,self.Size):
            print(self.Arr[i])

    def Summation(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]

        return Sum






def main():
    obj = Numbers()

    obj.Accept()
    obj.Display()
    Ret = obj.Summation()
    print("Summation of all elements is :",Ret)

    

    

if __name__=="__main__":
    main()