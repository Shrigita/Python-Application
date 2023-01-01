def Display(Value):
   cnt = 0
   while(Value > cnt):
      print("*",end ='\t')
      cnt = cnt + 1
      
   print()
  
def main():
   print("Enter Number :")
   No =int(input())
   Display(No) 

if __name__ == "__main__":
    main()