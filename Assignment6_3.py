
class Arithematic:
    def __init__(self,A):
        print("Inside init method")
        self.Value = A
        

    def ChkPrime(self):
        i = 0
        for i in range(2,int(self.Value /2)+1):
            if(self.Value % i == 0):
                break
        
        if (i == int(self.Value/2)):
            return True
        

    def ChkPerfect(self):
        Ans = self.SumofFactors()

        if (self.Value ==Ans):
            return True


    def Factors(self):
        list1 =[]
        for i in range(1,int((self.Value)/2) + 1):
            if(self.Value % i == 0):
                list1.append(i)
            
        print(list1)
                
                
        

    def SumofFactors(self):
        Sum = 0
        for i in range(1,int((self.Value)/2) + 1):
            if(self.Value % i == 0):
                Sum = Sum + i 
                 
        return Sum
        

def main():
    print("Inside main method")
    print("Enter Number :")
    No = int(input())

    obj = Arithematic(No)

    Ret = obj.ChkPrime()
    if (Ret ==True):
        print("Number is Prime")
    else:
        print("Number is not Prime")

    Ret1 = obj.ChkPerfect()
    if (Ret1 ==True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    obj.Factors()

    Ret2 = obj.SumofFactors()
    print("Sum of Factors :",Ret2)

if __name__ =="__main__":
    print("Inside starter")
    main()