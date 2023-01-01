class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()  #[]
        self.Accept()
   
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

    def Average(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]

        return (Sum/self.Size)

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if (self.Arr[i] > Max):
                Max = self.Arr[i]
        
        return Max
            
    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0,self.Size):
            if (self.Arr[i] < Min):
                Min = self.Arr[i]
        
        return Min
        
def main():
    obj = Numbers()
    
    obj.Display()

    Ret = obj.Summation()
    print("Summation of all elements is :",Ret)

    Ret = obj.Average()
    print("Average of all elements is :",Ret)

    Ret = obj.Maximum()
    print("largest element is :",Ret)

    Ret = obj.Minimum()
    print("smallest element is :",Ret)
    

    

if __name__=="__main__":
    main()