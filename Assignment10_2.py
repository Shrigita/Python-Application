from sys import *
import os


def ChangeFileExtension(Dir_Name,Extension1,Extension2):
    res =[]
    
    for file1 in os.listdir(Dir_Name):
        if file1.endswith(Extension1):
            res.append(file1)
            
    print(res)
    
    for file2 in os.listdir(Dir_Name):
        old_name =os.path.join(Dir_Name,file2)
        new_name =old_name.replace(Extension1,Extension2)
        os.rename(old_name,new_name)
    print("Change Extension successsfully")
    
   
    

def main():
    print("------------------------Automation---------------------")
    print("Application Name :",argv[0])
    if(len(argv) < 3):
        print("Insufficent Argument..")
        exit()

    if( argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This Script will travel the directory and display the same extenson file name and change the extension of this file")
        exit()

    if( argv[1] == "-u" or argv[1] == "-U"):
        print("Usage :Application_Name Directiry_Name Firstextension SecondExtension")
        exit()

    ChangeFileExtension(argv[1],argv[2],argv[3])
    
if __name__ =="__main__":
    main()