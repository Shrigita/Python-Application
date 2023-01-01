import os

def Delete_File(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
    else: 
        print("there is no such file")
        
def main():
    print("Enter file Name to delete:")
    Name = input()

    Delete_File(Name)

if __name__ =="__main__":
    main()