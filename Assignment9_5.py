from sys import *
import os

def Check_String(FileName1,string):
    print("Inside Check_String Function")
    fd = open(FileName1,"r")
    lines = fd.read()
    cnt = 0
    
    if string in lines:
        print("String is exit in file")
        print("Frequency of word :",lines.count(string))
    else : 
        print("not exit")   
    
    fd.close()

    
def main():
    print("Inside Main Function :")
    file1 = argv[1]
    string = argv[2]
    Check_String(file1,string)

if __name__ == "__main__":
    main()
