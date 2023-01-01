import math
class BankAccount:
    RIO = 10.5
    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Name of User :",self.Name)
        print("Amount :",self.Amount)
    
    def Deposit(self,Amount):
        self.Amount += self.Amount
        return self.Amount
       
    def Withdraw(self,amount):
        self.Amount -=amount
        return self.Amount
        
    def CalculateInterest(self):
        interest = self.Amount * (BankAccount.RIO /100)
        self.Amount += interest
        return self.Amount

def main():
    print("Enter User Name :")
    user = input()
    print("Enter Amount :")
    Amount1 = int(input())

    obj = BankAccount(user,Amount1)

    print("Enter Deposit Amount :")
    Dep = int(input())
    iRet = obj.Deposit(Dep)
    print("Total amount is :",iRet)

    print("Enter Withdraw Amount :")
    wid= int(input())
    iRet = obj.Withdraw(wid)
    print("Total amount is :",iRet)

    Ret = obj.CalculateInterest()
    print("Total Amount with interest :",Ret)

    print("-----------------------------------")
    obj.Display()
    print("-----------------------------------")
if __name__ =="__main__":
    main()

    
