print(" Display Number is even or odd")

import MarvellousModule

def main():
    print("Enter Number:")
    x=int(input())

    Ret =MarvellousModule.Number(x)

    if Ret == True:
        print("Number is even")
    if Ret == False:   
        print("Number is odd")


if __name__ == "__main__":
    main()

print("End of Program")    