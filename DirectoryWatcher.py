import os
from sys import *

def Directory_Watcher(Dir_Name):
    print("Inside Directory Watcher Method")
    print("Name of input Directory :",Dir_Name)

    for foldername,subfolder,Filename in os.walk(Dir_Name):
        print("Folder name is :"+foldername)
        for subf in subfolder:
            print("Subfolder name is :"+foldername+"is"+subf)
        for fnames in Filename:
            print("File inside folder"+foldername+"is"+fnames)
        print(" ")

def main():
    print("Directory watcher Application :")

    if(len(argv) < 2):
        print("Insufficient Arfument")
        exit()

    if(argv[1] == "-h"):
        print("This Script will travel the directory and display the file name")
        exit()

    if(argv[1]== "-u"):
        print("Usage :Application_Name Directiry_Name")
        exit()

    Directory_Watcher(argv[1])

if __name__ =="__main__":
    main()