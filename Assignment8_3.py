def Display(Value):
    cnt = 0
    while(Value > cnt):
        print(Value,end="\t")
        Value = Value - 1

      
    print()

def main():
   print("Enter Number :")
   No =int(input())
   Display(No) 

if __name__ == "__main__":
    main()