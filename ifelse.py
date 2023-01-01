import MarvellousModule

def main():
    print("Enter First Number : ")
    no1 = int(input())
    print("Enter Second Number : ")
    no2 = int(input())

    Ret =MarvellousModule.NumberCheak(no1, no2)
     
    if Ret == no1 :
        print("greter Number :",no1)
        print("smaller Number :",no2)
    elif Ret == no2:
        print("greter Number :",no2)
        print("smaller Number :",no1)
    else:
        print("Both are same :")
    
if __name__== "__main__":
    main()
    
print("End of Program")