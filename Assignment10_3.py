from sys import *
import os
import shutil

def CopyDirectory(Dir_Name1 ,Dir_Name2):
    try:
        if not os.path.exists(os.path.dirname(Dir_Name2)):
            os.makedirs(os.path.dirname(Dir_Name2))
    except OSError as err:
        pass

    shutil.copytree(Dir_Name1,Dir_Name2)

    print("Copy file Successfully")
    
    


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

    CopyDirectory(argv[1],argv[2])
    
if __name__ =="__main__":
    main()