from sys import *
import shutil
import os

def Read_File(FileName1,FileName2):
    print("Inside Read File")

    if(os.path.exists(FileName1)):
        fd1 = open(FileName1,"r")
    else :
        print("File not exits")
    

    if(os.path.exists(FileName2)):
        fd2 = open(FileName2 ,"w") 
    else:
        print("File not exits")
    
    shutil.copyfile(FileName1,FileName2)
    print("File Copyed..........")
   
    fd1.close()
    fd2.close()
    
        
      


def main():
    print("Inside Main Function :")
    file1 =argv[1]
    file2 =argv[2]
    Read_File(file1,file2)

if __name__ =="__main__":
    main()