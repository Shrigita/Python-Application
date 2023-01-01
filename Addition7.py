print("Application to Demonstrate industrial Programming")

def Addition(value1, value2):
    Ans = value1 + value2
    return Ans

def main():
     print("Enter the First Number : ")
     no1 = int(input())
     
     print("Enter the Second Number : ")
     no2 = int(input())
    
     Ret = Addition(no1, no2)

     print("Addition is :",Ret)

if __name__ == "__main__":
      main()