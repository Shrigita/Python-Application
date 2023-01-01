import os

def CheckFile(FileName):
    if(os.path.exists(FileName)):
        print("File is exists")  
    else:
        print("File not exit") 
        
def main():
    print("Enter the file name to create")
    Name = input()

    CheckFile(Name)


if __name__ =="__main__":
    main()