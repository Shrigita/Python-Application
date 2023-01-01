
    
def main():
    print("Enter the Number:")
    Num = int(input())

    fact = 1
    for i in range(1,Num+1):
        fact = fact * i
    print("Factorial =",fact)
    
if __name__ == "__main__":
    main()