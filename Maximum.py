#Application to findout the Maximum Number

import MarvellousModule

def main():
    print("Please Enter First Number : ")
    No1 = input()

    print("Please Enter Second Number : ")
    No2= input()
    
    Ret = MarvellousModule.Maximum(int(No1),int(No2))

    print("Maximum Number is : ",Ret)
    
if __name__ == "__main__":
    main()
        