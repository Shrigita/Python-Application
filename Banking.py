#Instance Variable : Name,Account Number,Address,Amount
#Instance method :CreateAccount,DisplayAccountInfo
#class Vaiable :Bank_Name,ROI_ON_FD
#class Method :DisplayBankInformation
#static Method :DisplayKYCInfo

class Bank_Account:
    Bank_Name ="HDFC Bank PVT LTD"
    ROI_ON_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0.0

    def CreateAccount(self):
        print("Enter Your Name : ")
        self.Name =input()

        print("Enter Your Initial Amount : ")
        self.Amount =int(input())

        print("Enter Your Address : ")
        self.Address =input()

        print("Enter Your Account Number : ")
        self.AccountNo =float(input())

    def DisplayAccountInfo(self):
        print("------Your Account information in below-----------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number of Account Holder : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in Account : ",self.Amount)
        print("--------------------------------------------------")

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking Console")
        print("Name of our bank is :",Bank_Account.Bank_Name)
        print("Rate of intrest on Fixed Deposit : ",Bank_Account.ROI_ON_FD,"%")

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below  KYC information :")
        print("According to the rules of Goverment of india you have to sumbit below document")
        print("1:Passport size photo")
        print("2:photo of adhar card")
        print("3:Photo of PAN Card")

    def Deposit(self,Value):
        self.Amount = self.Amount + Value
       

    def withdraw(self,Value):
        self.Amount = self.Amount - Value

def main():
    Bank_Account.DisplayKYCInfo()

    print("Name of Bank :",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit :",Bank_Account.ROI_ON_FD,"%")

    Bank_Account.DisplayBankInformation()

    user1 = Bank_Account()
    user2 = Bank_Account()

    print("Creating the First Account")
    user1.CreateAccount()

    print("Creating the Second Account")
    user2.CreateAccount()

    user1.DisplayAccountInfo()
    user2.DisplayAccountInfo()

    
    user1.Deposit(1000)
    user2.Deposit(2000)

    print("Amount of {} after deposit is {}:".format(user1.Name,user1.Amount))
    print("Amount of {} after deposit is {}:".format(user2.Name,user2.Amount))
     
    user1.withdraw(500)
    user2.withdraw(500)

    print("Amount of {} after withdraw is {}:".format(user1.Name,user1.Amount))
    print("Amount of {} after withdraw is {}:".format(user2.Name,user2.Amount))
     
    


if __name__=="__main__":
    main()