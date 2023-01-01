from sys import *
import os
import shutil
import fnmatch

def CopyFile(Dir_Name1 ,Dir_Name2,Extension):
    try:
        if not os.path.exists(os.path.dirname(Dir_Name2)):
            os.makedirs(os.path.dirname(Dir_Name2))
    except OSError as err:
        pass

    for foldername, subfolder, Filenames in os.walk(Dir_Name1):
        for fnames in Filenames:
            if fnames.endswith(Extension):
                shutil.copy2(fnames,Dir_Name2)
            else:
                pass

           
        print(" Copy............")

def main():
    print("------------------------Automation---------------------")
    print("Application Name :",argv[0])
    if(len(argv) < 3):
        print("Insufficent Argument..")
        exit()

    if( argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This Script will travel the directory and display the same extenson file name")
        exit()

    if( argv[1] == "-u" or argv[1] == "-U"):
        print("Usage :Application_Name Directiry_Name extension")
        exit()

    CopyFile(argv[1],argv[2],argv[3])
    
if __name__ =="__main__":
    main()