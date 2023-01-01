print("Welcome to Fibonacciseries")

def main():
    a = 0
    b = 1

    print("Enter Number limit")
    num = int(input())
    

    print("Fibonacciseries is :")
    while a <= num  :
        print(a, end =',')
        a, b = b, a+b
        

if __name__ == "__main__":
    main()
    