from sys import *
import shutil
import os

def Check_SameFile(FileName1,FileName2):
    print("Inside Check_FileSame Function")

    fd1 = open(FileName1,"r")
    fd2 = open(FileName2,"r")

    fd1_lines = fd1.readline()
    fd2_lines = fd2.readline()

    for i in range (len(fd1_lines)):
        if fd1_lines[i] != fd2_lines[i]:
            print("File not match")

    print("File is Same")   

    fd1.close()
    fd2.close()

def main():
    print("Inside Main Function :")
    file1 = argv[1]
    file2 = argv[2]
    Check_SameFile(file1,file2)

if __name__ == "__main__":
    main()