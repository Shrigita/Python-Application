import MarvellousModule

def main():
     print("Enter the First Number : ")
     no1 = int(input())
     
     print("Enter the Second Number : ")
     no2 = int(input())
    
     Ret1 = MarvellousModule.Add(no1, no2)
     print("Addition is :",Ret1) 

     Ret2 = MarvellousModule.Sub(no1, no2)
     print("Subtraction is :",Ret2)

     Ret3 = MarvellousModule.Mult(no1, no2)
     print("Multiplication is :",Ret3)

     Ret4 = MarvellousModule.Div(no1, no2)
     print("Division is :",Ret4)
     
if __name__ == "__main__":
      main()