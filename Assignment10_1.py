from sys import *
import os

def DisplayFileSearch(Dir_Name ,Extension):
    res =[]
    for file1 in os.listdir(Dir_Name):
        if file1.endswith(Extension):
            res.append(file1)

    print(res)


def main():
    print("------------------------Automation---------------------")
    print("Application Name :",argv[0])
    if(len(argv) < 2):
        print("Insufficent Argument..")
        exit()

    if( argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This Script will travel the directory and display the same extenson file name")
        exit()

    if( argv[1] == "-u" or argv[1] == "-U"):
        print("Usage :Application_Name Directiry_Name extension")
        exit()

    DisplayFileSearch(argv[1],argv[2])
    
if __name__ =="__main__":
    main()