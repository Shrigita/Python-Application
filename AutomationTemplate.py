from sys import *

def Script_Task(No):
    if((No % 2)==0):
        print("It is even number")
    else:
        print("It is odd number")


def main():
    print("--------------Shrigita Automation---------------")

    print("Automation script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : this script is used to perform ------")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ___number of argument as")
        print("First Argument as :______")
        print("Second Argument as :______")
        exit()

    else:
        Script_Task(int(argv[1]))
        #print("There is no such option in the script as :",argv[1])

if __name__ == "__main__":
    main()