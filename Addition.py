from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    print("Welcome to :",argv[0])
    if(len(argv) == 2):
        if(argv[1]=="--U") or (argv[1]=="--u"):
            print("Use the application as : ")
            print("python Name_Of_Application First_number Second_number")
            exit()

        if(argv[1]=="--H") or (argv[1]=="--h"):
            print("Help : This application is used to perform addition of 2 numbers")
            exit()

    if(len(argv)!=3):
        print("Invalid Number of argument")
        exit()

    Ret = Addition(int(argv[1]),int(argv[2]))
    print("Addition : ",Ret)

    
    print("Thank you for using the application")


    
if __name__ == "__main__":
    main()