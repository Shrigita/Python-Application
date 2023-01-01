print("Welcome")

def main():
    print("Please Enter Number : ")
    No = int(input())
    
    i = 0
    for i in range(2,int(No /2)+1):
        if(No % i == 0):
            break
        
    if (i == int(No/2)):
        print("Prime Number")
    else:
        print("Not Prime")
    
if __name__=="__main__":
    main()
        
